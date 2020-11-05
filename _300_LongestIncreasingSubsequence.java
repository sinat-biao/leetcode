package com.leetcode.java;

import java.util.Arrays;

class Solution300 {
    public int lengthOfLIS(int[] nums) {
        // 方法一：动态规划
        //
        if (nums.length == 0) {
            return 0;
        }
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        System.out.println(Arrays.toString(dp));
        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                dp[i] = 1;
            } else {
                for (int j = 0; j < i; j++) {
                    if (nums[j] < nums[i]) {
                        dp[i] = Math.max(dp[i], dp[j] + 1);
                    }
                }
                if (max < dp[i]) {
                    max = dp[i];
                }
            }
        }
        System.out.println(Arrays.toString(dp));
        return max;
    }

    public int lengthOfLIS2(int[] nums) {
        // 方法二：暴力搜索
        // 直接双重循环一次搜索以数组中每个元素开头的最大子序列，同时在子序列遍历的过程中，
        // 由于可能会存在后面结果好于前面的结果，所以需要记录当前 baseline 和 pre 的值，
        // 当遇到 nums[i] < baseline 但是 nums[i] > pre 的情况，则此时后面很可能有更大的子序列，需要跳过当前 baseline
        if (nums.length == 0) {
            return 0;
        }
        int len = nums.length;
        int maxsublen = 1;
        for (int i = 0; i < len; i++) {
            int sublen = 1;
            int baseline = nums[i];
            int pre = nums[i];
            for (int j = i + 1; j < len; j++) {
                if (nums[j] > baseline) {
                    sublen++;
                    pre = baseline;
                    baseline = nums[j];
                }
                if (j-2 >= 0 && nums[j] > pre && nums[j] < nums[j-1]) {
                    baseline = nums[j];
                }
            }
            if (sublen > maxsublen) {
                maxsublen = sublen;
            }
        }
        return maxsublen;
    }
}

public class _300_LongestIncreasingSubsequence {
    public static void main(String[] args) {
        int[] s = new int[]{10,9,2,5,3,7,101,18};
        Solution300 solution300 = new Solution300();
        System.out.println(solution300.lengthOfLIS(s));
        System.out.println(solution300.lengthOfLIS(new int[] {10, 9, 2, 5, 3, 4}));
        System.out.println(solution300.lengthOfLIS(new int[] {1,3,6,7,9,4,10,5,6}));
    }
}
