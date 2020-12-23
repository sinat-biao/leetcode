package com.example.leetcode;

class Solution64 {
    public int minPathSum(int[][] grid) {
        // ����һ����̬�滮
        // ���ö�ά�����¼ÿ�������С·��ֵ dp[i][j]
        // ״̬ת�Ʒ��̣�dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        // �߽�������
        // 1. dp[0][0] = grid[0][0]
        // 2. dp[0][j] = dp[0][j-1] + grid[0][j]
        // 3. dp[i][0] = dp[i-1][0] + grid[i][0]
        // ���˳�򣺴����ϵ�����

        int m = grid.length;
        int n = grid[0].length;
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j && i == 0) {
                    dp[i][j] = grid[i][j];
                } else if (i == 0) {
                    dp[i][j] = dp[i][j-1] + grid[i][j];
                } else if (j == 0) {
                    dp[i][j] = dp[i-1][j] + grid[i][j];
                } else {
                    dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
                }
            }
        }
        return dp[m-1][n-1];
    }
}

public class _64_MinimumPathSum {

}
