'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 方法一：暴力法（python 提交超出时间限制）
        # 穷举所有的水容量
        # max_ = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         if height[i] < height[j]:
        #             cont = (j-i) * height[i]
        #         else:
        #             cont = (j-i) * height[j]
        #         if max_ < cont:
        #             max_ = cont
        # return max_
    
        # 方法二：双指针法
        # 两个指针分别从左右向中间交替移动，每次移动时让小的一边的指针移动（以为容量主要取决于短板），
        # 并且每次移动都计算一次水容量与当前最大值进行比较。
        i = 0
        j = len(height) - 1
        max_ = 0
        while i < j:
            if height[i] < height[j]:
                cont = (j - i) * height[i]
                i += 1
            else: 
                cont = (j - i) * height[j]
                j -= 1
            if max_ < cont:
                max_ = cont
        return max_
    
        # 方法三：
        
    
S = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(S.maxArea(height))