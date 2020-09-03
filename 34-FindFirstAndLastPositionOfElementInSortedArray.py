"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 方法一：二分搜索
        # 因为数组有序，又要求时间复杂度为 O(logn)，所以采用二分法。
        # 又要求找出最左和最右的 target 数，所以在二分法查找到目标值时的逻辑需要做一些修改。
        # 具体为，同时向左和向右直到遇到左右两端不同的数之前，就停止。
        # i = 0
        # j = len(nums) - 1
        # while i <= j:
        #     mid = int((i + j) / 2)
        #     if nums[mid] == target:
        #         start = mid
        #         end = mid
        #         while start > 0 and nums[start] == nums[start-1]:
        #             start -= 1
        #         while end < len(nums)-1 and nums[end] == nums[end+1]:
        #             end += 1
        #         return [start, end]
        #     else:
        #         if nums[mid] > target:
        #             j = mid - 1
        #         if nums[mid] < target:
        #             i = mid + 1
        # return [-1, -1]
    
        # 方法二：暴力遍历
        # start = -1
        # end = -1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         if start == -1:
        #             start = i
        #         end = i
        # return [start, end]


S = Solution()
nums = [5,7,7,8,8,10]   
target = 8
print(S.searchRange(nums, target))  # [3,4]
nums = [5,7,7,8,8,10]
target = 6
print(S.searchRange(nums, target))  # [-1,-1]
nums = [1]
target = 1
print(S.searchRange(nums, target))  # [0,0]
nums = [3,3,3]
target = 3
print(S.searchRange(nums, target))  # [0,2]