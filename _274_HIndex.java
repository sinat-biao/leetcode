package com.leetcode.java;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;

class Solution274 {
    public int hIndex(int[] citations) {
        // 方法一：排序
        if (citations.length == 0) {
            return 0;
        }
        if (citations.length == 1) {
            if (citations[0] > 1) {
                return 1;
            } else {
                return citations[0];
            }
        }
        Arrays.sort(citations);
        // 逆序
        int i = 0;
        int j = citations.length - 1;
        while (i < j) {
            int tmp = citations[i];
            citations[i] = citations[j];
            citations[j] = tmp;
            i++;
            j--;
        }
        System.out.println(Arrays.toString(citations));
        int h = 0;
        for (i = 0; i < citations.length; i++) {
            if (citations[i] >= i + 1) {
                h = i + 1;
            }
        }
        return h;
    }
}

public class _274_HIndex {
    public static void main(String[] args) {
        Solution274 solution274 = new Solution274();
        System.out.println(solution274.hIndex(new int[] {0,1,3,5,6})); // 3
        System.out.println(solution274.hIndex(new int[]{0,1,3}));   // 1
        System.out.println(solution274.hIndex(new int[]{0,1,3,3}));     // 2
        System.out.println(solution274.hIndex(new int[]{0,1,1}));   // 1
        System.out.println(solution274.hIndex(new int[]{0,1,1,1})); // 1
        System.out.println(solution274.hIndex(new int[]{1})); // 1
    }
}
