'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''
import random
class Solution(object):
    def getrandom(self, count):  # 产生一个随机数
        return random.randint(0, count)

    def countnums(self, k, nums):  # 统计 k 在 nums 中的数量
        count = 0
        for i in nums:
            if i == k:
                count += 1
        return count
    
    def getcount(self, nums, num, left, right):
        count = 0
        for i in range(left, right + 1):
            if nums[i] == num:
                count += 1
        return count

    def majorityEleRec(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = int((right - left) / 2) + left
        left_num = self.majorityEleRec(nums, left, mid)
        right_num = self.majorityEleRec(nums, mid+1, right)
        if left_num == right_num:
            return left_num
        left_c = self.getcount(nums, left_num, left, right)
        right_c = self.getcount(nums, right_num, left, right)
        if left_c > right_c:
            return left_num
        else:
            return right_num
    
    def majorityElement(self, nums):
        # 方法一：两遍哈希法
        # 利用哈希表记录所有元素出现的次数，最后从中挑选出最高的那个
        # dict_num = {}
        # for i in nums:
        #     if dict_num.get(i) != None:
        #         dict_num[i] += 1
        #     else:
        #         dict_num[i] = 1
        # # print(dict_num)
        # max_nums = 0
        # key_nums = 0
        # for key, value in dict_num.items():
        #     if value > max_nums:
        #         max_nums = value
        #         key_nums = key
        # return key_nums
    
        # 方法二：一遍哈希
        # 同时扫描，同时添加，同时比较
        # dict_num = {}
        # max_num = 0
        # key_num = nums[0]
        # for i in nums:
        #     if dict_num.get(i) == None:
        #         dict_num[i] = 1
        #     else:
        #         dict_num[i] += 1
        #         if max_num < dict_num[i]:
        #             max_num = dict_num[i]
        #             key_num = i
        # return key_num
    
        # 方法三：先排序，在再比较是否超过一半
        # nums.sort()
        # conut = 1
        # for i in range(len(nums)-1):
        #     if nums[i+1] == nums[i]:
        #         conut += 1
        #         if conut > int(len(nums) / 2):
        #             return nums[i]
        #     else:
        #         count = 1
        # return nums[0]
        
        # 方法四：排序法改进（这思路巧妙!）
        # 排好序后，众数因为超过一半，所以数组中间位置的数一定是众数
        # nums.sort()
        # return nums[int(len(nums) / 2)]
    
        # 方法五：随机数法（这算法有点骚！）
        # 随机选一个数，计算其出现的次数，若超过一半，则为众数，否则重复挑选。
        # len_ = len(nums)
        # while True:
        #     r = self.getrandom(len_ - 1)    # 返回的数字作为下标
        #     r_nums = self.countnums(nums[r], nums)
        #     if r_nums > len_ / 2:
        #         return nums[r]
        
        # 方法六：分治
        # 二分数组，计算左右两边的众数，若相等则返回该众数，否则需要比较两个数在各自子数列中出现的次数，选择次数较大的作为众数；
        # 递归的将输入二分，直到子数列只有一个元素，返回该元素.
        # return self.majorityEleRec(nums, 0, len(nums) - 1)
    
        # Boyer-Moore 投票算法（这思路巧妙！）
        # 用一个 candidate 代表当前数，用 count 计数 candidate 出现次数，重复就 +1， 否则 -1；重复如上步骤。
        candidate = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
        return candidate 
    
S = Solution()
nums = [3,2,3]
print(S.majorityElement(nums))
nums = [2,2,1,1,1,2,2]
print(S.majorityElement(nums))