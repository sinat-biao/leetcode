package com.example.leetcode;

class Solution309 {
    int maxsum = 0;
    public int maxProfit(int[] prices) {
        // ����һ���ݹ�(��ʱ)
        // ÿ��λ�����ĸ�״̬��ֹͣ(0)������(1)������(2)���䶳��(3)
//	     if (prices.length == 0) {
//	         return 0;
//	     }
//	     profitTools(prices, 0, 1, 1, -1);   // ��ͣ����
//	     profitTools(prices, 0, 1, 0, -1);    // ��ͣ��ͣ
//	     profitTools(prices, 0, 1, 0, 0);    // ������ͣ
//	     profitTools(prices, 0, 1, 2, 0);     // ��������
//	     return maxsum;

        // ����������̬�滮
        // ���컺������ dp[i] ����� i ��������Ŀǰ�ۼ���׬ȡ����
        // ״̬ת�Ʒ��̣�
        // dp[i] = max(dp[i-1], dp[i-3] + prices[i]-prices[i-1], dp[i-2])
        // �߽�������
	    // dp[0] = 0
        // dp[1] = max(0, prices[1]-prices[0])
        // dp[2] = max(dp[1], prices[2]-prices[1], prices[2]-prices[0])
//        if (prices.length == 0) {
//            return 0;
//        }
//        int[] dp = new int[prices.length];
//        int maxsum = 0;
//        for (int i = 0; i < prices.length; i++) {
//            if (i == 0) {
//                dp[i] = 0;
//            } else if (i == 1) {
//                dp[i] = Math.max(0, prices[i] - prices[0]);
//            } else if (i == 2) {
//                dp[i] = Math.max(dp[1], Math.max(prices[2]-prices[1], prices[2]-prices[0]));
//            } else {
//                dp[i] = dp[i-3] + Math.max(0, prices[i]-prices[i-1]);
//                // ֱ������һ�ε��������
//                for (int k = 0; k <= i; k++) {
//                    dp[i] = Math.max(dp[i], Math.max(0, prices[i]-prices[k]));
//                }
//                // ��ǰһ�������Ļ����ϣ�������һ�ε��������
//                for (int k = 1; k <= i - 3; k++) {
//                    for (int p = k+2; p <= i-1; p++) {
//                        dp[i] = Math.max(dp[i], dp[k] + prices[i] - prices[p]);
//                    }
//                }
//            }
//            maxsum = Math.max(maxsum, dp[i]);
//            System.out.print(dp[i] + " ");
//        }
//        return maxsum;
        
        // ����������̬�滮
        int length = prices.length;
        if (length == 0) {
            return 0;
        }
        int[][] dp = new int[length][3];
        dp[0][0] = -prices[0];
        dp[0][1] = 0;
        dp[0][2] = 0;
        for (int i = 1; i < length; i++) {
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][2]-prices[i]);
            dp[i][1] = dp[i-1][0]+prices[i];
            dp[i][2] = Math.max(dp[i-1][2], dp[i-1][1]);
        }
        return Math.max(dp[length-1][0], Math.max(dp[length-1][1], dp[length-1][2]));
    }

    public void profitTools(int[] prices, int sum, int idx, int state, int mairu) {
        if (idx == prices.length) {
            if (maxsum < sum) {
                maxsum = sum;
            }
            return;
        }
        if (state == 0) {
            profitTools(prices, sum, idx+1, 0, mairu);
            if (mairu == -1) {
                profitTools(prices, sum, idx+1, 1, mairu);
            } else {
                profitTools(prices, sum, idx+1, 2, mairu);
            }
        }
        if (state == 1) {
            profitTools(prices, sum, idx+1, 0, idx);
            profitTools(prices, sum, idx+1, 2, idx);
        }
        if (state == 2) {
            profitTools(prices, sum+prices[idx]-prices[mairu], idx+1, 3, -1);
        }
        if (state == 3) {
            profitTools(prices, sum, idx+1, 0, mairu);
            profitTools(prices, sum, idx+1, 1, mairu);
        }
    }
}

public class _309_BestTimeToBuyAndSellStockWithCooldown {

}
