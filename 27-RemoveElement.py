"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 方法一：暴力法
        # 先看小目标数存在多少个
        # count = 0
        # for i in nums:
        #     if i == val:
        #         count += 1
        # # 每次遇到目标数，将所有数向前移动，并将目标数放在最后
        # for i in range(count):
        #     for j in range(len(nums)):
        #         if nums[j] == val:
        #             for k in range(j+1, len(nums)):
        #                 nums[k-1] = nums[k]
        #             nums[len(nums)-1] = val
        # print(nums)
        # return(len(nums)-count)
    
        # 方法二：双指针法1
        # i 从左到右，j 从右到左，一旦 nums[i] == val，则从右往左找一个不等于 val 的数与其进行交换，直到 i,j 在数组中间汇合。
        # if len(nums) == 0:
        #     return 0
        # i = 0
        # j = len(nums) - 1
        # while j > i:
        #     if nums[j] == val:
        #         j -= 1
        #     else:
        #         if nums[i] == val:
        #             nums[i] = nums[j]
        #             nums[j] = val
        #         else:
        #             i += 1
        # print(nums)
        # if nums[i] == val:
        #     return i
        # else:
        #     return i + 1
        
        # 方法二：双指针法2
        # 在 1 的基础上，考虑到题目对非 val 数值没有要求，所以不必考虑 j 位置的值，所以删减了一些操作
        # i = 0
        # j = len(nums)
        # while i < j:
        #     if nums[i] == val:
        #         nums[i] = nums[j - 1]
        #         j -= 1
        #     else:
        #         i += 1
        # print(nums)
        # return j
        
        # 方法二：双指针法3
        # i, j 均从左到右，num[j] == val 就让 j++，直到不等，将 nums[j] 与 nums[i] 交换，并同时增加两个索引
        # 这种方法不考虑列表中的 val 数据，只是将非 val 数据移到了列表前部，后面剩余数据随意。
        # i = 0
        # for j in range(len(nums)):
        #     if nums[j] != val:
        #         nums[i] = nums[j]
        #         i += 1
        # print(nums)
        # return i
    
        # 方法三：利用 pop 和 insert 操作
        i = 0
        count = len(nums) - nums.count(val)
        while i < count:
            if nums[i] == val:
                nums.pop(i)
                nums.append(val)
            else:
                i += 1
        print(nums)
        return count
        
        

S = Solution()
nums = [3,2,2,3]
val = 3
print(S.removeElement(nums, val))
nums = [0,1,2,2,3,0,4,2]
val = 2
print(S.removeElement(nums, val))
nums = [2,2,2,2,3,0,4,2]
val = 2
print(S.removeElement(nums, val))
nums = []
val = 0
print(S.removeElement(nums, val))