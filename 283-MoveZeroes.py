'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 方法一：队列法
        # 将 0 元素弹出，然后从队尾加入
        # count = 0
        # i = 0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         count += 1
        #     else:
        #         i += 1
        # for i in range(count):
        #     nums.append(0)
        # return nums
    
        # 方法二：双指针法
        # 两个指针 i、j，i 停在 0 元素位置，j 向后搜索第一个不是 0 的元素，然后交换两者
        i = 0
        j = 0
        while i < len(nums) and j < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            j = i + 1
            while j < len(nums) and nums[j] == 0:
                j += 1
            if i < len(nums) and j < len(nums) and i < j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            i += 1
            j += 1
        return nums


S = Solution()
nums = [0,1,0,3,12]
print(S.moveZeroes(nums))
nums = [0,0,1]
print(S.moveZeroes(nums))
nums = [0,0]
print(S.moveZeroes(nums))
nums = [2,1]
print(S.moveZeroes(nums))
nums = [4,2,4,0,0,3,0,5,1,0]
print(S.moveZeroes(nums))
nums = [1,0]
print(S.moveZeroes(nums))
        