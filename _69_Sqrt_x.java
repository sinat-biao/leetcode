package com.leetcode.java;

class Solution69 {
    public int mySqrt(int x) {
        // 方法一：牛顿迭代法
        if (x < 0) {
            return -1;
        }
        double e = 1e-5;
        double x_ = x;
        double y_ = (x_ + x / x_) / 2;
        while (Math.abs(x_ - y_) > e) {
            x_ = y_;
            y_ = (x_ + x / x_) / 2;
        }
        return (int) x_;
    }

    public int mySqrt2(int x) {
        // 方法二：顺序搜索
        // 为防止越界，需使用长整型。
        long c = 0;
        while ((c + 1) * (c + 1) <= x) {
            c++;
        }
        return (int)c;
    }

    long sq = 0;
    public int mySqrt3(int x) {
        // 方法三：二分搜索
        // 直接从 0-x 之间展开二分搜索
        int first = 0;
        int last = x;
        int mid = x / 2;
        if (mid == 0) {
            return x;
        }

        search(first, last, x);
        return (int)sq;
    }

    public void search(int first, int last, int target) {
        if (first < last) {
            long mid = (first + last) / 2;
            System.out.println("first = " + first + " last = " + last + " mid = " + mid);
            if (mid * mid == target) {
                sq = mid;
                return;
            } else {
                if (mid * mid < target) {
                    sq = mid;
                    System.out.println("sq = " + sq);
                    search((int) (mid + 1), last, target);
                    return;
                } else {
                    search(first, (int) mid, target);
                    return;
                }
            }
        }
        return;
    }

    public int mySqrt4(int x) {
        // 方法四：二分查找
        int first = 0;
        int last = x;
        long mid;
        int ans = 0;
        while (first <= last) {
            mid = (first + last) / 2;
            if (mid * mid <= x) {
                ans = (int) mid;
                first = (int)mid + 1;
            } else {
                last = (int)mid - 1;
            }
        }
        return ans;
    }
}

public class _69_Sqrt_x {
    public static void main(String[] args) {
        int m = 4;
        Solution69 solution69 = new Solution69();
        System.out.println(solution69.mySqrt4(m));
        System.out.println(solution69.mySqrt4(8));
        System.out.println(solution69.mySqrt4(7));
        System.out.println(solution69.mySqrt4(2147395599));
        System.out.println(solution69.mySqrt4(2147395600));
    }
}
