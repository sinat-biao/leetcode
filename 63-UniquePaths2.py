"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 方法一：动态规划
        # 将障碍物处的值设为 -1，采用动态规划时一旦扫描到改位置，就将当前路径的值设为 -1，并直接跳到下个位置
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1]:
            return 0
        if m == 1 and n == 1:   # 特殊情况
            return 1
        dp = [[0]*n for i in range(m)]  # 需要采用这种赋值方式，dp2 = [[0] * 5 ]* 5 这种赋值方式会使得所有行指向同一地址，一改所有行对应位置同时改
        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                for k in range(i, m):
                    dp[k][0] = -1
                break
        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = 1
            else:
                for k in range(i, n):
                    dp[0][k] = -1
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = -1
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] == -1:
                    continue
                if dp[i-1][j] == -1:
                    if dp[i][j-1] == -1:
                        dp[i][j] = -1
                    else:
                        dp[i][j] = dp[i][j-1]
                elif dp[i][j-1] == -1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        if dp[m-1][n-1] < 0:
            return 0
        else:
            return dp[m-1][n-1]


S = Solution()
obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(S.uniquePathsWithObstacles(obstacleGrid))
obstacleGrid = [
  [1,0],
]
print(S.uniquePathsWithObstacles(obstacleGrid))
obstacleGrid = [
    [0,0],
    [1,1],
    [0,0]]
print(S.uniquePathsWithObstacles(obstacleGrid))
