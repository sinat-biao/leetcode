"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：暴力法
        # 穷尽搜索，利用双层循环，每次累加第二层循环的值，从中选择最大的
        # n = len(nums)
        # max_sum = min(nums)
        # for i in range(n):
        #     sub_sum = 0
        #     for j in range(i, n):
        #         sub_sum += nums[j]
        #         if sub_sum > max_sum:
        #             max_sum = sub_sum
        # return max_sum
    
        # 方法二：正数增益
        # 遍历数组，用一个 sum 记录当前的累加值，若将当前位置的数加到 sum 上使得 sum < 0，
        # 那么说明当前累加结果已经抵消了构成 sum 的连续值中的最大值带来的增益。
        # 此时直接将 sum 置为当前值，并在下一次累加时先判断 sum 是否小于 0，若小于，直接等于当前值，
        # 并继续后移并判断。否则将 sum 置为当前值，并继续累加过程。
        # sum = 0
        # ans = nums[0]
        # for i in range(len(nums)):
        #     if sum <= 0:
        #         sum = nums[i]
        #     else:
        #         sum += nums[i]
        #     ans = max([sum, ans])
        # return ans
    
        # 方法三：动态规划
        # 用 dp[i] 表示 nums 中以 nums[i] 结尾的最大子序和，然后每次更新时，以
        # dp[i] = max(dp[i-1] + nums[i], nums[i]) 来更新 dp[i]，即如果加和小于 nums[i]，
        # 说明累加值中有部分值对子序和产生负面影响，还不如 nums[i] 一个值贡献的多，
        # 那么就更新 dp[i] 为 nums[i]。
        dp = []
        dp.append(nums[0])
        max_ = dp[0]
        for i in range(1, len(nums)):
            dp.append(max([dp[i-1]+nums[i], nums[i]]))
            max_ = max(dp[i], max_)
        return max_
    
        # 方法四：分治
        # 请参见：https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-cshi-xian-si-chong-jie-fa-bao-li-f/
        # 不想写了
        

S = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(S.maxSubArray(nums))
nums = [1]
print(S.maxSubArray(nums))
nums = [0]
print(S.maxSubArray(nums))
nums = [-1]
print(S.maxSubArray(nums))
nums = [-2147483647]
print(S.maxSubArray(nums))