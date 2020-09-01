"""
Given an integer array nums sorted in ascending order, and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You should search for target in nums and if you found return its index, otherwise return -1.
"""
class Solution(object):
    
    def midsearch(self, nums, low, high, target):
        if low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            else:
                lift =  self.midsearch(nums, low, mid-1, target)
                if lift != -1:
                    return lift
                right = self.midsearch(nums, mid+1, high, target)
                if right != -1:
                    return right
                return -1
        else:
            return -1
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 方法一：普通搜索
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
    
        # 方法二：二分递归搜索
        # i = 0
        # j = len(nums) - 1
        # return self.midsearch(nums, i, j, target)
    
        # 方法三：二分搜索
        # 由于题目中数组原来升序且没有相同元素，然后按照某个轴点旋转了一次，
        # 这种特殊的数组在旋转一次后分为两段，由于没有重复元素，所以旋转后前一段的所有元素均比后一段大。
        # 这样在二分的时候就可以直接判断两端各自的端点值来判断两段哪一段有序。
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = int((i + j) / 2)
            if nums[mid] == target:
                return mid
            if i < mid and nums[i] <= nums[mid-1]:   # 左段有序
                # target 可能包含在左段
                if target >= nums[i] and target <= nums[mid-1]:   
                    j = mid - 1
                else:
                    i = mid + 1
            else:   # 右段有序
                if mid < j and target >= nums[mid+1] and target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return -1
        

S = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(S.search(nums, target))   # 4
nums = [4,5,6,7,0,1,2]
target = 3
print(S.search(nums, target))   # -1
nums = [1]
target = 0
print(S.search(nums, target))   # -1
nums = [1, 3]
target = 3
print(S.search(nums, target))   # 1
nums = [2,3,4,5,6,7,8,9,1]
target = 9
print(S.search(nums, target))   # 7