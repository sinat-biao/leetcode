"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：直接利用 python 函数
        # count = 0
        # i = 1
        # if len(nums) == 0:
        #     return 0
        # min_ = nums[0]-1
        # while i < len(nums):
        #     if nums[i] == min_:
        #         break
        #     if nums[i] == nums[i-1]:
        #         count += 1
        #         if count < 2:
        #             i += 1
        #         else:
        #             nums.pop(i)
        #             nums.append(min_)
        #     else:
        #         count = 0
        #         i += 1
        # print(nums)
        # return i
        
        # 方法二：双指针
        # 使用两个指针，一个快指针，一个慢指针。
        # 详情参见官方题解。
        j, count = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        print(nums)
        return j


S = Solution()
nums = [1,1,1,2,2,3]
print(S.removeDuplicates(nums))     # 5
nums = [0,0,1,1,1,1,2,3,3]
print(S.removeDuplicates(nums))
nums = [0,0,0,0,0]
print(S.removeDuplicates(nums))
nums = [-3,-1,0,0,0,3,3]
print(S.removeDuplicates(nums))
nums = []
print(S.removeDuplicates(nums))