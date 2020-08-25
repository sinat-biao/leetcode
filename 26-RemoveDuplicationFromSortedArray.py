"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：利用 python 的 set() 函数来进行去重操作
        # new_list = sorted(list(set(nums)))
        # for i in range(len(new_list)):
        #     nums[i] = new_list[i]
        # print(nums)
        # return len(new_list)
    
        # 方法二：双指针法
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        print(nums)
        return i + 1
        

S = Solution()
nums = [1,1,2]
print(S.removeDuplicates(nums))
nums = [0,0,1,1,1,2,2,3,3,4]
print(S.removeDuplicates(nums))
nums = [-1,0,0,0,0,3,3]
print(S.removeDuplicates(nums))
            