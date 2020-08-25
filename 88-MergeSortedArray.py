"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """    
        # 方法一：覆盖 nums1
        # for i in range(m, len(nums1)):
        #     nums1[i] = nums2[i-m]
        # nums1.sort()
        # return nums1
        
        # 方法二：双指针法（从前往后）
        # 并利用空间换时间（程序直接返回 nums1，所以需要改动 nums1
        # nums_copy = nums1.copy()
        # # 注意：python2 中没有 copy() 函数，所以需要使用下句复制
        # # nums_copy = [i for i in nums1]
        # p, p1, p2 = 0, 0, 0
        # while p1 < m and p2 < n:
        #     if nums_copy[p1] <= nums2[p2]:
        #         nums1[p] = nums_copy[p1]
        #         p += 1
        #         p1 += 1
        #     else:
        #         nums1[p] = nums2[p2]
        #         p += 1
        #         p2 += 1
        # if p1 < m:
        #     nums1[p:] = nums_copy[p1:m]
        # if p2 < n:
        #     nums1[p:] = nums2[p2:]
        # return nums1
    
        # 方法三：双指针法（从后往前）
        # 直接利用 nums1 后面的空位，无需额外的空间消耗
        p, p1, p2 = len(nums1)-1, m-1, n-1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
        if p2 >= 0:
            nums1[0:p2+1] = nums2[0:p2+1]
        return nums1
                
                
    
S = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(S.merge(nums1, 3, nums2, len(nums2)))
nums1 = [0]
nums2 = [1]
print(S.merge(nums1, 0, nums2, len(nums2)))
# print(nums1[:3] + nums2)