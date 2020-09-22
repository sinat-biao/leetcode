"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 方法一：动态规划
        # 用数组 dp 来记录最短路径累加值，dp[i][j] 代表当前位置的路径最小累计值，因为只能向下、向右移动，
        # 所以其值可以看作是 dp[i-1][j] 与 dp[i][j-1] 中较小的加上 grid[i][j] 的值。
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return grid[0][0]
        dp = [[0]*n for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        print(dp)
        return dp[m-1][n-1]

        # 方法二：
    
S = Solution()
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(S.minPathSum(grid))
grid = [
  [1],
]
print(S.minPathSum(grid))
grid = [
  [1, 2],
]
print(S.minPathSum(grid))