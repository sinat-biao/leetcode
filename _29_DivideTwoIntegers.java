package com.leetcode.java;

class Solution29 {
    public int divide(int dividend, int divisor) {
        // 方法一：绝对值累加
        if (dividend == 0) {
            return 0;
        } else if ((divisor == 1 || divisor == -1) && (dividend == Integer.MAX_VALUE || dividend == Integer.MIN_VALUE)) {
            if (dividend == Integer.MAX_VALUE && divisor == 1) {
                return Integer.MAX_VALUE;
            } else if (dividend == Integer.MAX_VALUE && divisor == -1) {
                return -Integer.MAX_VALUE;
            } else if (dividend == Integer.MIN_VALUE && divisor == 1) {
                return Integer.MIN_VALUE;
            } else {
                return Integer.MAX_VALUE;
            }
        } else if ((dividend < 0 && divisor < 0) || (dividend > 0 && divisor > 0)) {
            long ldividend = Math.abs((long)dividend);
            long ldivisor = Math.abs((long)divisor);
            long count = 0;
            long sum = 0;
            while (true) {
                sum = sum + ldivisor;
                if (sum > ldividend) {
                    System.out.println(count);
                    return (int)count;
                }
                count++;
            }
        } else {
            long dividend_ab = Math.abs((long)dividend);
            long divisor_ab = Math.abs((long)divisor);
            long count = 0;
            long sum = 0;
            while (true) {
                sum = sum + divisor_ab;
                if (sum > dividend_ab) {
                    return (int)-count;
                }
                count++;
            }
        }
    }
}

public class _29_DivideTwoIntegers {
    public static void main(String[] args) {
        Solution29 solution29 = new Solution29();
        int dividend = 10, divisor = 3;
        System.out.println(solution29.divide(dividend, divisor));
        System.out.println(solution29.divide(7, -3));
        System.out.println(solution29.divide(0, 1));
        System.out.println(solution29.divide(1, 1));
        System.out.println(solution29.divide(-1, 1));
        System.out.println(solution29.divide(-2147483648, -1));
        System.out.println(solution29.divide(-2147483648, 1));
        System.out.println(solution29.divide(-2147483648, 2));
        System.out.println(solution29.divide(2147483647, 2));
    }
}
