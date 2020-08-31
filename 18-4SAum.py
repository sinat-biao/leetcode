"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
Note:
The solution set must not contain duplicate quadruplets.
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 方法一：依次后向扫描
        # 先对数据排序，然后用4个指针i,j,m,n 按序向后扫描，j 从 i+1 开始，m 从 j+1 开始，n 从 m+1 开始。
        # if len(nums) < 4:
        #     return []
        # nums.sort()
        # # print(nums)
        # foursum_list = []
        # for i in range(len(nums)):
        #     if nums[i] >= 0 and nums[i] > target:
        #         break
        #     if i > 0 and nums[i] == nums[i-1]:  # 跳过重复元素
        #         continue
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] >= 0 and  nums[i] + nums[j] > target:
        #             break
        #         if j > i + 1 and nums[j] == nums[j-1]:  # 跳过重复元素
        #             continue
        #         for m in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[m] >= 0 and nums[i] + nums[j] + nums[m] > target:
        #                 break
        #             if m > j + 1 and nums[m] == nums[m-1]:  # 跳过重复元素
        #                 continue
        #             for n in range(m+1, len(nums)):
        #                 if n > m+1 and nums[n] == nums[n-1]:    # 跳过重复元素
        #                     continue
        #                 if nums[i] + nums[j] + nums[m] + nums[-1] < target:
        #                     break
        #                 if nums[i] + nums[j] + nums[m] + nums[n] > target:
        #                     break
        #                 if nums[i] + nums[j] + nums[m] + nums[n] == target:
        #                     foursum_list.append([nums[i], nums[j], nums[m], nums[n]])
        #         j += 1
        # return foursum_list
    
        # 方法二：双指针法
        # 先排序，然后 i，j 保持循环。
        # m，n 同时在一个循环中从两端向中间靠近
        if len(nums) < 4:
            return []
        nums.sort()
        print(nums)
        foursum_list = []
        len_ = len(nums)
        for i in range(len_):
            if nums[i] >= 0 and nums[i] > target:
                break
            if i > 0 and nums[i] == nums[i-1]:  # 跳过重复元素
                continue
            for j in range(i+1, len_):
                twosum = nums[i] + nums[j]
                if twosum >= 0 and twosum > target:
                    break
                if j > i + 1 and nums[j] == nums[j-1]:  # 跳过重复元素
                    continue
                m = j + 1
                n = len_ - 1
                target_new = target - nums[i] - nums[j]
                while m < n:
                    while m > j + 1 and m < n and nums[m] == nums[m-1]:
                        m += 1
                        # continue
                    while n < len_ - 1 and m < n and nums[n] == nums[n+1]:
                        n -= 1
                        # continue
                    if m < n and nums[m] + nums[n] == target_new:
                        foursum_list.append([nums[i], nums[j], nums[m], nums[n]])
                        m += 1
                        n -= 1
                        continue
                    if m < n and nums[m] + nums[n] > target_new:
                        n -= 1
                        continue
                    if m < n and nums[m] + nums[n] < target_new:
                        m += 1
                        continue
        return foursum_list
            

S = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(S.fourSum(nums, target))  # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
nums = [-3,-2,-1,0,0,1,2,3]
target = 0
print(S.fourSum(nums, target))  # [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
nums = [0,0,0]
target = 0
print(S.fourSum(nums, target))  # []
nums = [0,0,0,0]
target = 0
print(S.fourSum(nums, target))  # [[0, 0, 0, 0]]
nums = [5,5,3,5,1,-5,1,-2]
target = 4
print(S.fourSum(nums, target))  # [[-5, 1, 3, 5]]
nums = [1,-2,-5,-4,-3,3,3,5]
target = -11
print(S.fourSum(nums, target))  # [[-5, -4, -3, 1]]
nums = [-1,-5,-5,-3,2,5,0,4]
target = -7
print(S.fourSum(nums, target))  # [[-5, -5, -1, 4], [-5, -3, -1, 2]]
nums = [-1,2,2,-5,0,-1,4]
target = 3
print(S.fourSum(nums, target))  # [[-5,2,2,4],[-1,0,2,2]]