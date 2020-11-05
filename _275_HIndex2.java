package com.leetcode.java;

// 这题感觉时间都浪费在理解题意上了，我去你的意义。
// 直接见题解。

class Solution275 {
    public int hIndex(int[] citations) {
        // 方法一：顺序搜索
        int idx = 0, n = citations.length;
        for(int c : citations) {
            if (c >= n - idx) return n - idx;
            else idx++;
        }
        return 0;
    }
}

public class _275_HIndex2 {
    public static void main(String[] args) {
        Solution275 solution275 = new Solution275();
        System.out.println(solution275.hIndex(new int[]{0,1,3,5,6}));
        System.out.println(solution275.hIndex(new int[]{0,1,3}));
        System.out.println(solution275.hIndex(new int[]{0,1,3,3}));
        System.out.println(solution275.hIndex(new int[]{0,1,1}));
        System.out.println(solution275.hIndex(new int[]{0,1,1,1}));
    }
}
