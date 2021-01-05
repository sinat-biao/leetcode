package com.example.leetcode;

class NumMatrix {

    // int[][] matrix_;

    int[][] dp;

    public NumMatrix(int[][] matrix) {
        // matrix_ = matrix;
        int m = matrix.length, n = 0;
        if (m > 0) {
            n = matrix[0].length;
        } else {
            n = 0;
        }
        dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    dp[i][j] = matrix[i][j];
                } else if (i == 0) {
                    dp[i][j] = dp[i][j-1] + matrix[i][j];
                } else if (j == 0) {
                    dp[i][j] = dp[i-1][j] + matrix[i][j];
                } else {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j];
                }
                System.out.print(dp[i][j] + " ");
            }
            System.out.println();
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        // ����һ��������
        // ÿ�����������¼���һ��������ĺ�
        // int sum = 0;
        // for (int i = row1; i <= row2; i++) {
        //     for (int j = col1; j <= col2; j++) {
        //         sum += matrix_[i][j];
        //     }
        // }
        // return sum;

        // ����������̬�滮
        // ���컺������ dp[i][j] ��ʾ�������������Ͻǵ� (i, j) �����������е��ۼӺ�
        // ��ô��(row1, col1) �� (row2, col2) ֮����ۼӺͿɱ�ʾΪ��
        // dp[r2][c2] - dp[r1][c2] - dp[r2][c1] + dp[r1][c1]
        // ���� dp[][] ���鹹��Ĺ��̣��䶯̬ת�Ʒ������£�
        // dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + m[i][j]
        // �߽������� 
        // dp[0][0] = m[0][0]
        // dp[i][0] = dp[i-1][0] + m[i][0]
        // dp[0][j] = dp[0][j-1] + m[0][j]
        // if (dp.length == 0) {
        //     return 0;
        // }
        if (row2 == 0 && col2 == 0) {
            return dp[0][0];
        } else if (row2 == 0) {
            if (col1 == 0) {
                return dp[row2][col2];
            } else {
                return dp[row2][col2] - dp[row2][col1-1];
            }
        } else if (col2 == 0) {
            if (row1 == 0) {
                return dp[row2][col2];
            } else {
                return dp[row2][col2] - dp[row1-1][col2];
            }
        } else {
            if (row1 == 0 && col1 == 0) {
                return dp[row2][col2];
            } else if (row1 == 0) {
                return dp[row2][col2] - dp[row2][col1-1];
            } else if (col1 == 0) {
                return dp[row2][col2] - dp[row1-1][col2];
            }
            return dp[row2][col2] - dp[row1-1][col2] - dp[row2][col1-1] + dp[row1-1][col1-1];
        }
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */

public class _304_RangeSumQuery2D_Immutable {

}
