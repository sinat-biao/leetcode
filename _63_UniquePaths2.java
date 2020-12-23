package com.example.leetcode;

class Solution63 {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        // 方法一：动态规划
        // 在 62 题的基础上增加了障碍物
        // 同样用一个二维数组记录每一个点的路径数 dp[][]
        // 状态转移方程仍为：
        // dp[i][j] = dp[i-1][j] + dp[i][j-1]
        // 但是由于有障碍物，所以障碍处的路径数为 0
        // 边界条件与 62 题相同
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] == 1){
                    dp[i][j] = 0;
                } else if (i == j && i == 0) {
                    dp[i][j] = 1;
                } else if (i == 0) {
                    dp[i][j] = dp[i][j-1];
                } else if (j == 0) {
                    dp[i][j] = dp[i-1][j];
                } else {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        return dp[m-1][n-1];
    }
}

public class _63_UniquePaths2 {

}
