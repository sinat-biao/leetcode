'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 方法一：利用python函数
        # list -> set -> list -> 比较前后两个 list 长度是否一致
        # nums2 = list(set(nums))
        # if len(nums) != len(nums2):
        #     return True
        # else:
        #     return False
        
        # 方法二：哈希法
        # 扫描数组并向哈希表中添加元素，若存在冲突，说明有重复元素
        # hash_dict = {}
        # for i in range(len(nums)):
        #     if hash_dict.get(nums[i]):
        #         return True
        #     else:
        #         hash_dict[nums[i]] = 1
        # return False
        
        # 方法三：排序法
        # 先对数组排序，然后只要找是否有连续一样的值即可
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        
        
S = Solution()
nums = [1,2,3,1]
print(S.containsDuplicate(nums))
nums = [1,2,3,4]
print(S.containsDuplicate(nums))
nums = [1,1,1,3,3,4,3,2,4,2]
print(S.containsDuplicate(nums))