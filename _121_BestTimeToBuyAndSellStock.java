package com.example.leetcode;

class Solution {
    int ret = 0;
    public int maxProfit(int[] prices) {
        // 方法一：暴力法
//        if (prices.length == 0) {
//            return ret;
//        }
//        for (int i = 0; i < prices.length; i++) {
//            for (int j = i + 1; j < prices.length; j++) {
//                if (prices[j] - prices[i] > ret) {
//                    ret = prices[j] - prices[i];
//                }
//            }
//        }
//        return ret;

        // 方法二：动态规划(一次遍历)
        // 状态转移方程：f(n) = max(f(n-1), prices[n]-min(prices[0, n-1]))
        if (prices.length <= 1) {
            return ret;
        }
        if (prices.length == 2) {
            return Math.max(0, prices[1] - prices[0]);
        }
        ret = Math.max(0, prices[1] - prices[0]);
        int min = Math.min(prices[1], prices[0]);
        for (int i = 2; i < prices.length; i++) {
            ret = Math.max(ret, prices[i] - min);
            min = Math.min(min, prices[i]);
        }
        return ret;
    }
}

public class _121_BestTimeToBuyAndSellStock {

}
