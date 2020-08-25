'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
'''
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：去除法
        # list -> set -> list，然后依次推出前三个数
        # nums = list(set(nums))
        # if len(nums) < 3:
        #     return max(nums)
        # max_ = 0
        # for i in range(3):
        #     max_ = max(nums)
        #     nums.pop(nums.index(max_))
        # return max_
    
        # 方法二：排序法
        # 现将所有元素排序，然后找出第三大的数
        nums.sort()
        nums.reverse()
        print(nums)
        if len(nums) < 3:
            return nums[0]
        count = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                count += 1
            if count == 2:
                return nums[i+1]
        return nums[0]
    
    
S = Solution()
nums = [3, 2, 1]
print(S.thirdMax(nums))
nums = [1, 2]
print(S.thirdMax(nums))
nums = [2, 2, 3, 1]
print(S.thirdMax(nums))