'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：排序
        # 直接排序，然后按序计数，若当前计数值与对应的元素值不同，就返回
        # nums.sort()
        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        # return len(nums)
    
        # 方法二：按序查找
        # 依次查找 0-n，哪个不存在，就是哪个
        # for i in range(len(nums) + 1):
        #     if not nums.__contains__(i):
        #         return i
            
        # 方法三：哈希查找
        # 先将所有元素填入哈希表，然后查找哈希表
        # nums = set(nums)
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i
            
        # 方法四：求和对比
        # 先求出 0-n 个数的累加和，然后累加数组中的所有数，最后比较这两个数的差。
        sum1 = int((0 + len(nums) + 1) * len(nums) / 2)
        sum2 = 0
        for i in nums:
            sum2 += i
        return sum1 - sum2    
            
        
S = Solution()
nums = [3,0,1]
print(S.missingNumber(nums))
nums = [9,6,4,2,3,5,7,0,1]
print(S.missingNumber(nums))
nums = [0, 1, 2, 3, 4, 5]       # 6
print(S.missingNumber(nums))
nums = [0]                      # 1
print(S.missingNumber(nums))