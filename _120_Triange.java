package com.example.leetcode;

import java.util.List;

class Solution120 {
    // int ret = Integer.MAX_VALUE;
    public int minimumTotal(List<List<Integer>> triangle) {
        // 方法一：递归(超时)
        // 每层往下，有两个路径
        // 停止条件：
        // 超过最大层数
        // if (triangle.size() == 0) {
        //     return ret;
        // }
        // minimumTotalTools(triangle, 0, 0, 0);
        // return ret;

        // 方法二：动态规划
        // 利用二维数组缓存所有位置的最小累加值：dp[level][idx]
        // 状态转移方程：dp[level][idx] = Math.Min(dp[level-1][idx], dp[level-1][idx-1]) + triange[level][idx]
        // 边界条件：
        // dp[0][0] = triange[0][0]
        // dp[level][level.length-1] = dp[level-1][idx-1]
        int m = triangle.size();
        if (m == 0) {
            return 0;
        }
        int mins = Integer.MAX_VALUE;
        int n = triangle.get(m-1).size();
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < triangle.get(i).size(); j++) {
                if (i == 0) {
                    dp[i][j] = triangle.get(i).get(j);
                } else if (j == 0) {
                    dp[i][j] = dp[i-1][j] + triangle.get(i).get(j);
                } else if (j == triangle.get(i).size() - 1) {
                    dp[i][j] = dp[i-1][j-1] + triangle.get(i).get(j);
                } else {
                    dp[i][j] = Math.min(dp[i-1][j], dp[i-1][j-1]) + triangle.get(i).get(j);
                }

                if (i == m -1) {
                    if (mins > dp[i][j]) {
                        mins = dp[i][j];
                    }
                }
            }
        }
        // 打印
        // for (int i = 0; i < m; i++) {
        //     for (int j = 0; j < triangle.get(i).size(); j++) {
        //         System.out.print(dp[i][j] + " ");
        //     }
        //     System.out.println();
        // }
        // int mins = dp[m-1][0];
        // for (int k = 1; k < triangle.get(m-1).size(); k++) {
        //     if (mins > dp[m-1][k]) {
        //         mins = dp[m-1][k];
        //     }
        // }
        return mins;

        // 方法三：方法二改进
        // 由于只需要最大值，所以只需要一维数组即可，每次覆盖前面一层元素即可
        // 同时需要从后往前覆盖，因为下一层的值需要依赖前一层从前往后的值
    }

    // public void minimumTotalTools(List<List<Integer>> triangle, int level, int idx, int sum) {
    //     //
    //     if (level >= triangle.size()) {
    //         if (sum < ret) {
    //             ret = sum;
    //         }
    //         return;
    //     }
    //     minimumTotalTools(triangle, level+1, idx, sum+triangle.get(level).get(idx));
    //     minimumTotalTools(triangle, level+1, idx+1, sum+triangle.get(level).get(idx));
    // }
}



public class _120_Triange {
	


}
