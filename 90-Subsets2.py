"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
"""
class Solution(object):
    def regsearch(self, nums, subsets, t, k, tp):
        if k == len(nums):
            return
        for i in range(k, len(nums)):
            if tp != nums[i]:
                t.append(nums[i])
                subsets.append([k for k in t])
                self.regsearch(nums, subsets, t, i+1, tp)
                if len(t) > 0:
                    tp = t.pop()
    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 方法一：递归
        # 相对于 78-Subset，这里的递归多了一个判断条件，因为数组有重复元素，所以在执行后续的添加时，
        # 需要判断上次出栈的元素是否与这次加入的元素相同，若相同，则跳过。
        nums.sort()
        subsets = []
        t = []
        subsets.append(t)
        self.regsearch(nums, subsets, t, 0, min(nums)-1)
        return subsets


S = Solution()
nums = [1,2,2]
print(S.subsetsWithDup(nums))
nums = [5,5,5,5,5]
print(S.subsetsWithDup(nums))
nums = [1,1,2,2]
print(S.subsetsWithDup(nums))
nums = [0]
print(S.subsetsWithDup(nums))
nums = [4,4,4,1,4]
print(S.subsetsWithDup(nums))