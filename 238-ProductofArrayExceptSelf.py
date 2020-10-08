"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
"""
class Solution(object):
    def proofsubarr(self, nums):
        pro = 1
        for i in nums:
            pro *= i
        return pro
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 方法一：遍历相乘（超时）
        # pro_arr = []
        # for i in range(len(nums)):
        #     pro_arr.append(self.proofsubarr(nums[:i] + nums[i+1:]))
        # return pro_arr
    
        # 方法二：构造左右乘积列表
        # 用两个数组 pre_pro、net_pro 分别记录从左到右、从右到左的累乘值，
        # 然后每次计算除当前元素之外的乘积时，计算公式为：
        # pro[i] = pre_pro[i-1] * net_pro[i+1]
        n = len(nums)
        pre_pro = []
        net_pro = []
        p_pro = 1
        n_pro = 1
        for i in range(n):
            p_pro *= nums[i]
            pre_pro.append(p_pro)
        for i in range(n-1, -1, -1):
            n_pro *= nums[i]
            net_pro.insert(0, n_pro)
        print(pre_pro)
        print(net_pro)
        pro_arr = []
        for i in range(n):
            if i == 0:
                pro_arr.append(net_pro[i+1])
            elif i == n-1:
                # print(pre_pro[i-1])
                pro_arr.append(pre_pro[i-1])
            else:
                pro_arr.append(pre_pro[i-1]*net_pro[i+1])
        return pro_arr

S = Solution()
nums = [1,2,3,4]
print(S.productExceptSelf(nums))
nums = [4,3,2,1,2]
print(S.productExceptSelf(nums))
        