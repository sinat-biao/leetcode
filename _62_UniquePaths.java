package com.example.leetcode;

class Solution62 {
    public int uniquePaths(int m, int n) {
        // ����һ����̬�滮
        // ������ά���� dp[i][j] ��¼ÿ��λ�õ�·����
        // dp[i][j] = dp[i-1][j] + dp[i][j-1]
        // �߽�������
        // 1. dp[0][j] = dp[0][j-1]
        // 2. dp[i][0] = dp[i-1][0]
        // 3. dp[0][0] = 1;
        // ���˳�򣺴����ϵ����£�����ѭ������Ϊ��
        // for (int i = 0; i < m; i++) 
        //     for (int j = 0; j < n; j++)

        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j && i == 0) {
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

public class _62_UniquePaths {

}
