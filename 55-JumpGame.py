"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
"""
class Solution(object):
    def max_and_idx(self, nums):
        max_ = nums[0]
        max_idx = 0
        for i in range(len(nums)):
            if max_ <= nums[i]:
                max_ = nums[i]
                max_idx = i
        return max_, max_idx
    
    def jumprec(self, nums, sum_step, current_idx):
        if sum_step + nums[current_idx] >= len(nums):
            return True
        else:
            if nums[current_idx] == 0:
                return False
            else:
                for i in range(1, nums[current_idx]+1):
                    ist = self.jumprec(nums, sum_step+i, current_idx+i)
                    if not ist:
                        continue
                    else:
                        return True
                return False
    
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 方法一：递归遍历 (python 中超时了)
        # 用一个 sum_step 记录总共走的步数，每次将当前能走的的步数都尝试一边，看最后能否走到最后（即 sum_step >= len(nums)）
        # sum_step = 1
        # cantoend = self.jumprec(nums, sum_step, current_idx=0)
        # return cantoend
    
        # 方法二：直接判断能否跳过0
        # 直接检查数组中的 0 元素，若能跳过当前的零元素，则可以，否则不行
        # zero_idx_list = []
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         zero_idx_list.append(i)
        # if len(zero_idx_list) == 0:
        #     return True
        # for i in zero_idx_list:
        #     canjump = False
        #     # print(i)
        #     for j in range(i+1):
        #         if nums[j] + j > i:
        #             canjump = True
        #         if nums[j] + j == i and i == len(nums) - 1:
        #             canjump = True
        #     if canjump:
        #         continue
        #     else:
        #         return False
        # return True
        
        # 方法三：贪心
        # 当前最大可以到达的位置记录下来，然后遍历数组，如果当前位置最大到达位置超过原来的，就更新最大到达位置。
        # 如果最大到达位置超过达到数组长度，就返回 Ture，否则继续遍历；遍历结束返回 False。
        rightmost = 0
        for i in range(len(nums)):
            if i <= rightmost:
                rightmost = max(rightmost, nums[i] + i)
            if rightmost >= len(nums) - 1:
                return True
        return False

        
S = Solution()
nums = [2,3,1,1,4]  
print(S.canJump(nums))  # True
nums = [3,2,1,0,4]
print(S.canJump(nums))  # False
nums = [0]
print(S.canJump(nums))  # True
nums = [2, 0]
print(S.canJump(nums))  # True
nums = [2,0,0]
print(S.canJump(nums))  # True
nums = [5,9,3,2,1,0,2,3,3,1,0,0]
print(S.canJump(nums))  # True
