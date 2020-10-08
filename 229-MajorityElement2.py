"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 方法一：排序遍历
        # 先将数组排序，此时相同的元素靠在一起，依次扫描技术，当相同元素技术大于 n / 3，
        # 则说明此元素是个众数。另外，为了防止 [2,2] 这种两次判断情况，在第一个 if 语句中加入重复性检验语句。
        # nums.sort()
        # count = 1
        # sub = []
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         count += 1
        #         if count > int(len(nums) / 3):
        #             if len(sub) == 0:
        #                 sub.append(nums[i])
        #             else:
        #                 if sub[-1] != nums[i]:
        #                     sub.append(nums[i])
        #     else:
        #         count = 1
        #         if count > int(len(nums) / 3):
        #             sub.append(nums[i])
        # return sub
    
        # 方法二：一次哈希
        # 遍历数组，每次将当前元素插入哈希表计数，然后在哈希表中找出众数即可
        hashset = dict()
        n = len(nums)
        z = int(n / 3)
        sub = []
        for i in range(n):
            if nums[i] in hashset:
                hashset[nums[i]] += 1
            else:
                hashset[nums[i]] = 1
        print(hashset)
        for key, val in hashset.items():
            if val > z:
                sub.append(key)
        return sub


S = Solution()
nums = [3,2,3]
print(S.majorityElement(nums))
nums = [1]
print(S.majorityElement(nums))
nums = [1, 2]
print(S.majorityElement(nums))
nums = [2,2]
print(S.majorityElement(nums))