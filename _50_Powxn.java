package com.leetcode.java;

class Solution50 {
    public double myPow(double x, int n) {
        // 方法一：累乘累除(超时)
        if (n > 0) {
            if (x == 1) {
                return 1;
            }
            if (x == -1) {
                long abs = Math.abs((long)n);
                if (abs % 2 == 0) {
                    return -1;
                } else {
                    return 1;
                }
            }
            int count = 1;
            double sum = x;
            while (count < n) {
                sum = sum * x;
                count++;
            }
            return sum;
        } else if (n < 0) {
            if (x == 1) {
                return 1;
            }
            if (x == -1) {
                if (Math.abs((long)n) % 2 == 0) {
                    return 1;
                } else {
                    return -1;
                }
            }
            int count = 1;
            double sum = 1 / x;
            while (count < Math.abs((long)n)) {
                sum = sum / x;
                count++;
            }
            return sum;
        } else {
            return 1;
        }
    }

    public double myPow2(double x, int n) {
        // 方法二：二分
        long N = n;
        if (N >= 0) {
            return quickMul(x, N);
        } else {
            return 1 / quickMul(x, -N);
        }
    }

    public double quickMul(double x, long N) {
        if (N == 0) {
            return 1;
        }
        double y = quickMul(x, N / 2);
        if (N % 2 == 0) {
            return y * y;
        } else {
            return y * y * x;
        }
    }
}

public class _50_Powxn {
    public static void main(String[] args) {
        Solution50 solution50 = new Solution50();
        System.out.println(solution50.myPow2(2, 10));
        System.out.println(solution50.myPow2(2.1, 3));
        System.out.println(solution50.myPow2(2, -2));
        System.out.println(solution50.myPow2(2, Integer.MIN_VALUE));
        System.out.println(Math.pow(2.0, Integer.MIN_VALUE));
    }
}
