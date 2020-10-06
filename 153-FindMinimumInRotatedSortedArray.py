"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：排序后取第一个元素
        # nums.sort()
        # return nums[0]

        # 方法二：二分查找
        # 数组旋转后分为有序的两段，可以在有序的两端中搜索第一个元素并进行比较
        start = 0
        end = len(nums)
        i = start
        j = end - 1
        min_ = nums[i]
        while i <= j:
            mid = int((i + j) / 2)
            print('---', mid, nums[mid])
            if nums[mid] < min_:
                min_ = nums[mid]
                print(min_)
            # 左边有序
            if i < mid and nums[i] <= nums[mid - 1]:
                if nums[i] < min_:
                    min_ = nums[i]
                else:
                    i = mid + 1
            else:
                if mid < j and nums[mid+1] < min_:
                    min_ = nums[mid+1]
                else:
                    j = mid - 1
        return min_

S = Solution()
# nums = [3,4,5,1,2] 
# print(S.findMin(nums))
# nums = [4,5,6,7,0,1,2]
# print(S.findMin(nums))
# nums = [5,6,7,8,9,0,1,2,3,4]
# print(S.findMin(nums))
nums = [1]
print(S.findMin(nums))
nums = [2,3,4,5,6,7,8,9,1]
print(S.findMin(nums))
