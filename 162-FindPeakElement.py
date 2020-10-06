"""
A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：普通遍历
        # if len(nums) == 1:
        #     return 0
        # for i in range(len(nums)):
        #     if i > 0 and i < len(nums) - 1 and nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        #         return i
        # if nums[0] > nums[len(nums) - 1]:
        #     return 0
        # else:
        #     return len(nums) - 1
        
        # 方法二：二分查找
        # 这里只需找到一个峰值即可，不需要对峰值的大小有所要求，所以可以直接通过二分查找寻找符合条件：
        # nums[mid] > nums[mid-1] and numd[mid] > nums[mid+1] 的位置即可。
        # 每次二分时，只需要判断当前位置的斜率即可，若斜率上升：nums[mid] < nums[mid+1]，则右边肯定有一个峰值；
        # 若 nums[mid-1] > nums[mid]，则左边肯定有一个峰值。
        start = 0
        end = len(nums) - 1
        i = start
        j = end
        while i <= j:
            mid = int((i + j) / 2)
            if i < mid and mid < j and nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            if i == mid and mid < j and nums[mid] > nums[mid + 1]:
                return mid
            if j == mid and i < mid and nums[mid] > nums[mid-1]:
                return mid
            if i == j and i == mid:
                return mid
            # 峰值可能在左边
            if i < mid and nums[mid] < nums[mid-1]:
                j = mid - 1
            else:   # 峰值可能在右边
                if mid < j and nums[mid+1] > nums[mid]:
                    i = mid + 1
        return 0
    
        
S = Solution()
nums = [1,2,3,1]
print(S.findPeakElement(nums))
nums = [1,2,1,3,5,6,4]
print(S.findPeakElement(nums))
nums = [1]
print(S.findPeakElement(nums))
nums = [3,2,1]
print(S.findPeakElement(nums))
nums = [1,2,3]
print(S.findPeakElement(nums))