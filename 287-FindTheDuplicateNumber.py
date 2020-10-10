"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one duplicate number in nums, return this duplicate number.
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：先排序，然后找重复值
        # nums.sort()
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         return nums[i]
        
        # 方法二：遍历搜索（超时）
        # i = 0
        # j = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]
        
        # 方法三：二分搜索
        # 参看题解
        
    

S = Solution()
nums = [1,3,4,2,2]
print(S.findDuplicate(nums))
nums = [3,1,3,4,2]
print(S.findDuplicate(nums))
nums = [1,1]
print(S.findDuplicate(nums))
nums = [1,1,2]
print(S.findDuplicate(nums))
nums = [2,2,2,2,2]
print(S.findDuplicate(nums))