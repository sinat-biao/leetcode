"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：遍历（python中超出时间限制）
        # pro = nums[0]
        # for i in range(len(nums)):
        #     pro2 = nums[i]
        #     if pro2 > pro:
        #         pro = pro2
        #     for j in range(i+1, len(nums)):
        #         pro2 = pro2 * nums[j]
        #         if pro2 > pro:
        #             pro = pro2
        # return pro
    
        # 方法二：动态规划
        # 当前位置 i 的乘积为之前位置上的最大乘积乘上当前位置元素与当前未知元素中较大者。
        # 但是本题有正负，所以可能存在负负得正但是被舍去而不参与比较的情况，所以同时维护一个最大、一个最小
        # 动态规划数组。具体可参见官方题解：
        pro_min = [nums[0]]*len(nums)
        pro_max = [nums[0]]*len(nums)
        print(pro_min)
        print(pro_max)
        for i in range(1, len(nums)):
            pro_min[i] = min(pro_min[i-1] * nums[i], pro_max[i-1] * nums[i], nums[i])
            pro_max[i] = max(pro_max[i-1] * nums[i], pro_min[i-1] * nums[i], nums[i])
        print(pro_min)
        print(pro_max)
        return max(max(pro_max), max(pro_min))
        

S = Solution()
nums = [2,3,-2,4]   
print(S.maxProduct(nums))   # 6
nums = [-2,0,-1]
print(S.maxProduct(nums))   # 0
nums = [0,2]
print(S.maxProduct(nums))   # 2
nums = [-3,0,1,-2]
print(S.maxProduct(nums))   # 1
nums = [-2,3,-4]
print(S.maxProduct(nums))   # 24
        