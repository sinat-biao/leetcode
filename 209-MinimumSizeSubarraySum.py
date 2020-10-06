"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
"""
class Solution(object):
    # 计算子数组的和
    def sumofsubarray(self, subarray):
        sum_ = 0
        for i in subarray:
            sum_ += i
        return sum_
    
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：双指针遍历（超时）
        # i = 0
        # j = 0
        # for k in range(len(nums)):  # 子数组的长度从 1 到 len(nums)
        #     i = 0
        #     j = i + k
        #     while j < len(nums):
        #         if self.sumofsubarray(nums[i:j+1]) >= s:
        #             return j - i + 1
        #         i += 1
        #         j += 1
        # return 0
    
        # 方法二：双指针交替移动
        # 设定 2 个指针 i、j，初始均指向数组首元素，开始 j 向后移动，直到累加值大于等于 s，
        # 比较数组的长度与之前的谁更短并更新。然后将 i 后移知道累加值小于 s，再次更新最小长度。
        # 循环此过程。
        i = 0
        j = 0
        sum_ = nums[i]
        min_len = len(nums)
        while j < len(nums):
            while j < len(nums) and sum_ < s:
                j += 1
                if j == len(nums):
                    break
                sum_ += nums[j]
                print('sum_ =', sum_)
            if i == 0 and sum_ < s:
                return 0
            if j == len(nums):
                break
            len_ = j - i + 1
            if len_ < min_len:
                min_len = len_
            print(len_)
            while i <= j and i < len(nums) and sum_ >= s:
                sum_ -= nums[i]
                i += 1
                len_ -= 1
                print('-',len_)
            len_ += 1
            if min_len > len_:
                min_len = len_    
        
        return min_len

S = Solution()
s = 7
nums = [2,3,1,2,4,3]
print(S.minSubArrayLen(s, nums))
s = 7
nums = [2,3,1]
print(S.minSubArrayLen(s, nums))
s = 4
nums = [1,4,4]
print(S.minSubArrayLen(s, nums))
            