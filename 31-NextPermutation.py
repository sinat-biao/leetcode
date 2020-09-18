"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
class Solution(object):
    
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 方法一：次小值替换 + 排序
        # 从后向前扫描，直到遇到 nums[i] > nums[i-1]，说明此处值需要实施进位操作；
        # 然后从 [i:] 之中选一个最小同时又比 nums[i-1] 的值大的值（这是防止出现选的值比 nums[i-1] 的值小，调换后整体值反而变小），
        # 将其与 nums[i-1] 交换，然后对 [i:] 排序。
        # 若扫描过程没有执行交换，说明当前序列已经最大（即已降序排列），那么直接返回升序序列。
        len_ = len(nums)
        is_change = False
        for i in range(len_-1, 0, -1):
            if nums[i] <= nums[i-1]:
                continue
            else:
                j = len_-1
                while nums[j] <= nums[i-1]:
                    j -= 1
                tmp = nums[j]
                nums[j] = nums[i-1]
                nums[i-1] = tmp
                # self.subsetsort(nums, i, len_-1)
                nums2 = nums[i:]
                nums2.sort()
                nums[i:] = nums2
                is_change = True
                break
        if not is_change:
            nums.sort()
        return nums
        
        # 方法二：方法一改进
        # 所用思想与方法一一致，仅将方法一中交换之后对 [i:]子序列的排序改为反转操作，这样额外空间开销更小。
        # 改动较小，无需重新实现。
        

S = Solution()
nums = [1,2,3]
print(S.nextPermutation(nums))  # [1, 3, 2]
nums = [3,2,1]
print(S.nextPermutation(nums))  # [1, 2, 3]
nums = [1,1,5]
print(S.nextPermutation(nums))  # [1, 5, 1]
nums = [1,2,3,4,5]
print(S.nextPermutation(nums))  # [1, 2, 3, 5, 4]
nums = [1,2,3,5,4]
print(S.nextPermutation(nums))  # [1, 2, 4, 3, 5]
nums = [1,2,5,3,4]
print(S.nextPermutation(nums))  # [1, 2, 5, 4, 3]
nums = [5,1,4,3,2]
print(S.nextPermutation(nums))  # [5, 2, 1, 3, 4]
nums = [1,3,2]
print(S.nextPermutation(nums))  # [2, 1, 3]
nums = [2,3,1]
print(S.nextPermutation(nums))  # [3, 1, 2]
nums = [1, 5, 1]
print(S.nextPermutation(nums))  # [5, 1, 1]
nums = [5,4,7,5,3,2]
print(S.nextPermutation(nums))  # [5,5,2,3,4,7]

# nums = [1,2,3,8,6,4,5]
# S.subsetsort(nums, 3, len(nums)-1)
# print(nums)