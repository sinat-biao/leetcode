'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] 
and the absolute difference between i and j is at most k.
'''
class Solution(object):
    
    def isContainsDuplicate(self, subnums):
        # 判断是否有重复数字
        subnums2 = list(set(subnums))
        if len(subnums) == len(subnums2):
            return False
        else:
            return True
        
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 方法一：滑动窗口（python 中超出时间限制）
        # 窗口间距始终保持在 k 以内，从左到右扫描列表
        # if len(nums) < k:
        #     return self.isContainsDuplicate(nums)
        # for i in range(len(nums)-k+1):
        #     # 切片的范围是 [i, j)
        #     if self.isContainsDuplicate(nums[i:i+k+1]):
        #         return True
        # return False
    
        # 方法二：哈希表（在 python 中超时了）
        # 每 k+1 个元素执行一次 hash 插入，判断有没有冲突，若有，返回 True；
        # 否则，清空 hash 表，后移一个元素，然后重复上述过程；
        # if len(nums) <= k:
        #     k = len(nums) - 1
        # for i in range(len(nums)-k):
        #     hashset = set()
        #     j = i
        #     while j <= i+k:
        #         if nums[j] in hashset:
        #             return True
        #         else:
        #             hashset.add(nums[j])
        #             # print(hashset)
        #         j += 1
        #     hashset.clear()
        # return False
        # 后面回头一看，此方法与方法一其实同一类型的思想，只不过区间判断重复的函数不同而已
    
        # 方法三：空间换时间
        # 这种方法不稳定，一旦当出现巨大的数时，将会有大量的无用空间被占用
        # if len(nums) == 0:
        #     return False
        # if len(nums) <= k:
        #     k = len(nums) - 1
        # dict_list = [0 for i in range(max(nums)+1)]
        # # print(dict_list)
        # i = 0
        # while i < k+1:
        #     if dict_list[nums[i]] == 0:
        #         dict_list[nums[i]] = 1
        #     else:
        #         return True
        #         # print(hashset)
        #     i += 1
        # dict_list[nums[0]] = 0
        # if len(nums) == k:
        #     return False
        # i = 1
        # j = i + k
        # while j < len(nums):
        #     if dict_list[nums[j]] != 0:
        #         return True
        #     else:
        #         dict_list[nums[j]] = 1
        #         dict_list[nums[i]] = 0
        #     i += 1
        #     j += 1
        # return False
    
        # 方法四：哈希算法改进
        # 在方法二的基础上改进，在 i-j 窗口滑动时，每次后移一个元素时，只有最后一元素是新的，只有最前一个元素被挤出，
        # 所以 hashset 不用全部清空，只需要把被挤出的元素删掉，并判断新入元素即可。
        if len(nums) == 0:
            return False
        if len(nums) <= k:
            k = len(nums) - 1
        hashset = set()
        for i in range(k+1):
            if nums[i] in hashset:
                return True
            else:
                hashset.add(nums[i])
        hashset.remove(nums[0])
        for i in range(1, len(nums)-k):
            j = i + k
            if nums[j] in hashset:
                return True
            else:
                hashset.add(nums[j])
            hashset.remove(nums[i])
        return False
        
                
S = Solution()
nums = [1,2,3,1]
k = 3
print(S.containsNearbyDuplicate(nums, k)) 
nums = [1,0,1,1]
k = 1
print(S.containsNearbyDuplicate(nums, k)) 
nums = [1,2,3,1,2,3]
k = 2
print(S.containsNearbyDuplicate(nums, k)) 
nums = [99, 99]
k = 2
print(S.containsNearbyDuplicate(nums, k)) 
nums = [99, 99]
k = 3
print(S.containsNearbyDuplicate(nums, k)) 
nums = [1]
k = 1
print(S.containsNearbyDuplicate(nums, k)) 
nums = [2147483647,-2147483648,2147483647,-2147483648]
k = 2
print(S.containsNearbyDuplicate(nums, k)) 
nums = []
k = 0
print(S.containsNearbyDuplicate(nums, k)) 