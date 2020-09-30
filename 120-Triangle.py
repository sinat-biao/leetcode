"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
"""
class Solution(object):            
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 方法一：动态规划
        # 复制一个 triangle 数组，每个位置记录用来到达当前位置的路径和，最后在最后一行选一个最小的.
        # 由于相邻位置的定义为下一行相同列和下一行后一列，所以每一行第一个和最后一个位置的路径和
        # 只能分别是上一行相同列+当前位置元素 和 上一行前一列+当前位置元素。每一行中间的位置的路径和
        # 则为上一行同列和后一列 + 当前位置中较小的。
        # row = len(triangle)
        # path_sum = [[0]*k for k in range(1, row+1)]
        # print(path_sum)
        # path_sum[0][0] = triangle[0][0]
        # for i in range(1, row):
        #     for j in range(len(triangle[i])):
        #         if j == 0:
        #             path_sum[i][j] = path_sum[i-1][0] + triangle[i][j]
        #         elif j == len(triangle[i]) - 1:
        #             path_sum[i][j] = path_sum[i-1][j-1] + triangle[i][j]
        #         else:
        #             sum1 = path_sum[i-1][j] + triangle[i][j]
        #             sum2 = path_sum[i-1][j-1] + triangle[i][j]
        #             path_sum[i][j] = min(sum1, sum2)
        # for i in path_sum:
        #     print(i)
        # return min(path_sum[row-1])
    
        # 方法二：方法一优化
        # 直接用一个长度与 triangle 最后一行相同的数组来存储路径和
        row = len(triangle)
        path_sum = [0]*len(triangle[row-1])
        print(path_sum)
        path_sum[0] = triangle[0][0]
        for i in range(1, row):
            # 从后往前覆盖
            for j in range(len(triangle[i])-1, -1, -1):
                if j == 0:
                    path_sum[j] = path_sum[0] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    path_sum[j] = path_sum[j-1] + triangle[i][j]
                else:
                    sum1 = path_sum[j] + triangle[i][j]
                    sum2 = path_sum[j-1] + triangle[i][j]
                    path_sum[j] = min(sum1, sum2)
        print(path_sum)
        return min(path_sum)
        
    
S = Solution()
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(S.minimumTotal(triangle))