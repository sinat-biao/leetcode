'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 方法一：向后依次搜索（双指针）
        # 先将数组排序，然后依次向后扫描找出符合条件的值。
        # i 从头到尾头，j 从 i+1 到尾，k 从 j+1 到尾，依次向后扫描
        # nums.sort()
        # min_ = 10000
        # min_sum = 0
        # # print(nums)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if abs(nums[i] + nums[j] + nums[k] - target) < min_:
        #                 min_sum = nums[i] + nums[j] + nums[k]
        #                 min_ = abs(nums[i] + nums[j] + nums[k] - target)
        # return min_sum

        # 方法二：改进的双指针
        # 在方法一的基础上，让 j、k 指针分别从 (i+1, n) 的两端向中间移动
        nums.sort()
        min_ = 10000
        min_sum = 0
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == target:
                    return target
                if abs(nums[i] + nums[j] + nums[k] - target) < min_:
                    min_sum = nums[i] + nums[j] + nums[k]
                    min_ = abs(nums[i] + nums[j] + nums[k] - target)
                if nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                    # 跳过重复值
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    # 跳过重复值
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return min_sum


S = Solution()
# nums = [-1, 2, 1, -4]
# target = 1
# print(S.threeSumClosest(nums, target))  # 2
# nums = [1, 1, 1, 0]
# target = -100
# print(S.threeSumClosest(nums, target))  # 2
# nums = [0, 2, 1, -3]
# target = 1
# print(S.threeSumClosest(nums, target))  # 0
# nums = [1, 1, -1, -1, 3]
# target = -1
# print(S.threeSumClosest(nums, target))  # -1
# nums = [1, 2, 4, 8, 16, 32, 64, 128]
# target = 82
# print(S.threeSumClosest(nums, target))  # 82
nums = [-1, 0, 1, 1, 55]
target = 3
print(S.threeSumClosest(nums, target))  # 2
