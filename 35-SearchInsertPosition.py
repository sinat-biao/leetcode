"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 方法一：常规搜索（从头到尾）
        # if len(nums) == 0:
        #     return 0
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        #     if nums[i] > target:
        #         return i
        #     if i == len(nums)-1 and nums[i] < target:
        #         return len(nums)
            
        # 方法二：利用 python 工具函数
        # if nums.__contains__(target):
        #     return nums.index(target)
        # else:
        #     nums.append(target)
        #     nums.sort()
        #     print(nums)
        #     return nums.index(target)
        
        # 方法三：二分查找
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low
        


S = Solution()
nums = [1,3,5,6]
target = 5
print(S.searchInsert(nums, target))
nums = [1,3,5,6]
target = 2
print(S.searchInsert(nums, target))
nums = [1,3,5,6]
target = 7
print(S.searchInsert(nums, target))                    
# nums = [1,3,5,6]
# print(nums.index(5))  
# print(nums.__contains__(7))              
        