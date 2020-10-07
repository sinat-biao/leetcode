"""
You are given a sorted unique integer array nums.
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # 方法一：顺序遍历
        n = len(nums)
        sub_arr = []
        i = 0
        j = 0
        while i < n and j < n:
            while j < n-1 and nums[j+1] == nums[j] + 1:
                j += 1
            if i == j:
                sub_arr.append("{i}".format(i = nums[i]))
            else:
                sub_arr.append("{i}->{j}".format(i=nums[i], j=nums[j]))
            i = j + 1
            if j < n:
                j += 1
        return sub_arr

    
S = Solution()
nums = [0,1,2,4,5,7]
print(S.summaryRanges(nums))
nums = [0,2,3,4,6,8,9]
print(S.summaryRanges(nums))
nums = []
print(S.summaryRanges(nums))
nums = [0]
print(S.summaryRanges(nums))