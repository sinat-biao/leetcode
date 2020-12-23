package com.example.leetcode;

class Solution63 {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        // ����һ����̬�滮
        // �� 62 ��Ļ������������ϰ���
        // ͬ����һ����ά�����¼ÿһ�����·���� dp[][]
        // ״̬ת�Ʒ�����Ϊ��
        // dp[i][j] = dp[i-1][j] + dp[i][j-1]
        // �����������ϰ�������ϰ�����·����Ϊ 0
        // �߽������� 62 ����ͬ
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
