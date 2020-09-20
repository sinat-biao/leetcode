"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
"""
class Solution(object):
    count = 0
    def itegoing(self, m, n, now_point):
        print(now_point)
        if now_point == [m-1, n-1]:
            self.count += 1
            print('-->', self.count)
            return True
        if now_point[0] < m-1:
            self.itegoing(m, n, [now_point[0]+1, now_point[1]])
        if now_point[1] < n-1:
            self.itegoing(m, n, [now_point[0], now_point[1]+1])
        return
        
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 方法一：递归遍历（python中超时）
        # 每个位置的下一步都有两种走法：向下、向右，递归遍历这种走法，直到到达终点。
        # now_point = [0, 0]
        # self.count = 0
        # self.itegoing(m, n, now_point)
        # return self.count
    
        # 方法二：排列组合（难想）
        # 因为该题只能向右、向下走，所以能走的路径是固定的。
        # 因为机器到底右下角，向下几步，向右几步都是固定的，
        # 比如，m=3, n=2，我们只要向下 2 步，向右 1 步就一定能到达终点。
        # 也即：从 m+n-2（总共要走的步数） 中 选出 m-1（纵向要走的步数） 个解即可
        # m_, n_, n_m = 1, 1, 1
        # for i in range(1, m+n-2+1):
        #     n_ *= i
        # for j in range(1, m-1+1):
        #     m_ *= j
        # for k in range(1, n-1+1):
        #     n_m *= k
        # return int(n_ / (m_ * n_m))
    
        # 方法三：动态规划 <套路是找到动态规划方程>
        # 设 dp[i][j] 为到达位置 (i,j) 的路径条数，其应为 dp[i-1][j] 与 dp[i][j-1] 之和，即动态规划方程为：
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        if m == 1 and n == 1:   # 特殊情况
            return 1
        dp = [[0]*n]*m
        for i in range(1, n):
            dp[0][i] = 1
        for i in range(1, m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

        
S = Solution()
m, n = 3, 2
print(S.uniquePaths(m, n))
m, n = 3, 7
print(S.uniquePaths(m, n))
m, n = 3, 3
print(S.uniquePaths(m, n))
m, n = 7, 3
print(S.uniquePaths(m, n))
m, n = 7, 7
print(S.uniquePaths(m, n))
m, n = 23, 12
print(S.uniquePaths(m, n))