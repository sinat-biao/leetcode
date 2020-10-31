package com.leetcode.java;

class Solution367 {
    public boolean isPerfectSquare(int num) {
        // 方法一：顺序查找(超时)
        for (int i = 0; i < num / 2; i++) {
            if (i * i == num) {
                return true;
            }
        }
        return false;
    }

    public boolean isPerfectSquare2(int num) {
        // 方法二：二分查找
        int first = 0;
        int last = num;
        long mid;
        while (first <= last) {
            mid = first + (last - first) / 2;
            if (mid * mid == num) {
                return true;
            } else {
                if (mid * mid < num) {
                    first = (int)mid + 1;
                } else {
                    last = (int)mid - 1;
                }
            }
        }
        return false;
    }
}

public class _367_ValidPerfectSquare {
}
