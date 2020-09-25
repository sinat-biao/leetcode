"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Follow up:
- Could you solve this problem without using the library's sort function?
- Could you come up with a one-pass algorithm using only O(1) constant space?
"""
class Solution(object):
    def quicksort(self, nums, start, end):
        i = start
        j = end
        if i < j:
            tmp = nums[i]
            while i < j:
                while i < j and nums[j] >= tmp:
                    j -= 1
                if i < j:
                    nums[i] = nums[j]
                    i += 1
                while i < j and nums[i] < tmp:
                    i += 1
                if i < j:
                    nums[j] = nums[i]
                    j -= 1
            nums[i] = tmp
            # print(nums, i, tmp)
            self.quicksort(nums, start, i - 1)
            self.quicksort(nums, i + 1, end)
        
    
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 方法一：快速排序
        # start = 0
        # end = len(nums) - 1
        # self.quicksort(nums, start, end)
        # return nums
    
        # 方法二：直接按序搜索元素
        # 因为只有 red（0）、white（1）、blue（2）三种颜色，所以可以直接从原数组中直接依次找出这些元素，加入新数组中即可
        # nums_copy = [k for k in nums]
        # nums.clear()    # 这一句在 python2 中会报错
        # count = 0
        # for i in range(len(nums_copy)):
        #     if nums_copy[i] == 0:
        #         nums[count] = 0
        #         count += 1
        # for i in range(len(nums_copy)):
        #     if nums_copy[i] == 1:
        #         nums[count] = 1
        #         count += 1
        # for i in range(len(nums_copy)):
        #     if nums_copy[i] == 2:
        #         nums[count] = 2
        #         count += 1
        # return nums
    
        # 方法三：荷兰国旗问题
        # 三个 p0、p2、curr 分别指向 0 的最右边界、2 的最左边界、当前元素。
        # curr 从左向右遍历，若当前元素为 0，将其与 p0 位置元素交换；若当前元素为 2，将其与 p2 位置元素交换；
        p0 = 0
        p2 = len(nums) - 1
        curr = p0
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr] = nums[p0]
                nums[p0] = 0
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                nums[curr] = nums[p2]
                nums[p2] = 2
                p2 -= 1
            else:
                curr += 1
        return nums


S = Solution()
nums = [2,0,2,1,1,0]
print(S.sortColors(nums))
nums = [2,0,1]
print(S.sortColors(nums))
nums = [0]
print(S.sortColors(nums))
        