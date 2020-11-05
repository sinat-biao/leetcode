package com.leetcode.java;

import java.util.ArrayList;

class Solution240 {
    public boolean searchMatrix(int[][] matrix, int target) {
        // 方法一：横向搜索+纵向搜索
        if (matrix.length == 0)  {
            return false;
        }
        int row = matrix.length;
        int col = matrix[0].length;
        for (int i = 0; i < row; i++) {
            if (col > 0 && matrix[i][0] <= target && matrix[i][col-1] >= target) {
                for (int j = 0; j < col; j++) {
                    if (matrix[i][j] == target) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public boolean searchMatrix2(int[][] matrix, int target) {
        // 方法二：走步搜索
        // 由题意，可以发现，该二维数组是从斜上方到斜下方递增排序的
        int row = matrix.length;
        if (row == 0) {
            return false;
        }
        int col = matrix[0].length;
        if (col == 0) {
            return false;
        }
        int i = row - 1;
        int j = 0;
        while (i >= 0 && j <= col - 1) {
            if (matrix[i][j] == target) {
                return true;
            }
            if (matrix[i][j] > target) {
                i--;
            } else {
                j++;
            }
        }
        return false;
    }
}

public class _240_SearchA2DMatrix2 {
    public static void main(String[] args) {
        Solution240 solution240 = new Solution240();
        int[][] matrix = new int[][] {{1,   4,  7, 11, 15},
                {2,   5,  8, 12, 19},
                {3,   6,  9, 16, 22},
                {10, 13, 14, 17, 24},
                {18, 21, 23, 26, 30}};
        System.out.println(solution240.searchMatrix2(matrix, 5));
    }
}
