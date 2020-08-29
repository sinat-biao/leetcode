"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
"""


class Solution(object):
    def containslist(self, new_list, str_set):
        # 通过 str 字符串判断是否存在
        str_ = ''
        for i in new_list:
            str_ += str(i)
        if str_ in str_set:
            return True
        else:
            return False

    def sum_digui(self, nums, list_sum, str_set):
        if len(nums) < 3:
            return
        print(nums)
        i = 0
        j = len(nums) - 1
        if (nums[i] < 0 and nums[j] < 0) or (nums[i] > 0 and nums[j] > 0):
            return
        for k in range(i + 1, j):
            if nums[i] + nums[j] + nums[k] == 0:
                new_list = [nums[i], nums[k], nums[j]]
                if not self.containslist(new_list, str_set):
                    list_sum.append(new_list)
                    str_set.add(str(nums[i]) + str(nums[k]) + str(nums[j]))
        # 递归
        j2 = j
        while i + 1 < j2 and nums[j2] == nums[j2 - 1]:
            j2 -= 1
        self.sum_digui(nums[i:j2], list_sum, str_set)
        i2 = i
        while i2 + 1 < j and nums[i2] == nums[i2 + 1]:
            i2 += 1
        self.sum_digui(nums[i2 + 1:j + 1], list_sum, str_set)

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 方法一：排序 + 递归（python 中超出时间限制）
        # 先对数组排序，小于0的在左端，大于0的在右端，用两个指针 i，j 从两头向中间移动，
        # 另外，指针 k 在 i-j 间移动遍历
        # list_sum = []
        # str_set = set()
        # nums.sort()
        # self.sum_digui(nums, list_sum, str_set)
        # return list_sum

        # 方法二：排序 + 双指针
        # 三个指针（实际是一重循环+两个指针）。将数组先排序，然后第一个指针 a 从左到右遍历，
        # 此时剩下两个指针的目标值变为 -nums[a]，然后第二个指针 b 从 a 之后向右遍历，同一轮中第三个指针 c 从右向左遍历，
        # 直到 b 和 c 扫描到目标值，或者 b、c 相遇，则 a 后移一位继续进行上述比较。
        nums.sort()
        sum_list = []
        for a in range(len(nums)):
            # 跳过相同的元素
            if a > 0 and nums[a - 1] == nums[a]:
                continue
            target = -nums[a]
            c = len(nums) - 1
            for b in range(a + 1, len(nums)):
                # 跳过相同元素
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                while b < c and nums[b] + nums[c] > target:
                    c -= 1
                if b == c:
                    break
                if target == nums[b] + nums[c]:
                    sum_list.append([nums[a], nums[b], nums[c]])
        return sum_list


S = Solution()
# nums = [-1, 0, 1, 2, -1, -4]    # [[-1, 0, 1], [-1, -1, 2]]
# print(S.threeSum(nums))
# nums = [0, 0, 0, 0]             # [[0, 0, 0]]
# print(S.threeSum(nums))
# nums = [-2, 0, 1, 1, 2]         # [[-2, 0, 2], [-2, 1, 1]]
# print(S.threeSum(nums))
# nums = [3, 0, -2, -1, 1, 2]     # [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
# print(S.threeSum(nums))
# nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]      # [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, 0, 2], [-2, -2, 4]]
# print(S.threeSum(nums))
# nums = [2, 0, -2, -5, -5, -3, 2, -4]
# print(S.threeSum(nums))
nums = [-13, 5, 13, 12, -2, -11, -1, 12, -3, 0, -3, -7, -7, -5, -3, -15, -2, 14, 14, 13, 6, -11, -11, 5, -15, -14, 5,
        -5, -2, 0, 3, -8, -10, -7, 11, -5, -10, -5, -7, -6, 2, 5, 3, 2, 7, 7, 3, -10, -2, 2, -12, -11, -1, 14, 10, -9,
        -15, -8, -7, -9, 7, 3, -2, 5, 11, -13, -15, 8, -3, -7, -12, 7, 5, -2, -6, -3, -10, 4, 2, -5, 14, -3, -1, -10,
        -3, -14, -4, -3, -7, -4, 3, 8, 14, 9, -2, 10, 11, -10, -4, -15, -9, -1, -1, 3, 4, 1, 8, 1]
print(S.threeSum(nums))
