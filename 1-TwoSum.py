"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 方法一、暴力法：
        # i 从左到右遍历，j 从 i 的下一个位置继续向右遍历，统计所有的求和。
        # 由于同一个数不能使用两次，所以j直接跳过i前的所有数（因为这些数在之前已经累加过了）。
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if i == j:
        #             continue
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # 方法二、两遍字典：
        # dict1 = {}
        # for i in range(len(nums)):
        #     dict1[nums[i]] = i
        # for i in range(len(nums)):
        #     component = target - nums[i]
        #     if dict1.get(component) and dict1[component] != i:
        #         return [i, dict1[component]]

        # 方法三、一遍字典：
        dict2 = {}
        for i in range(len(nums)):
            component = target - nums[i]
            if dict2.get(component) != None:
                return [dict2[component], i]
            dict2[nums[i]] = i


nums = [-3, 4, 3, 90]
target = 0
S = Solution()
print(S.twoSum(nums, target))
