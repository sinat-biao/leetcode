package com.example.leetcode;

import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;

class Solution264_zero {
    public int nthUglyNumber(int n) {
        // 方法一：暴力法(超时)
//        if (n <= 5) {
//            return n;
//        }
//        int ret = 0;
//        int i = 1;
//        int count = 0;
//        while (count < n) {
//            if (isUglyNumber(i)) {
//                ret = i;
//                count++;
//            }
//            i++;
//        }
//        return ret;

        // 方法二：方法一优化（超时）
        // 添加 set 存储已经计算得到的丑数，之后再通过遍历 (2, sqrt(i)) 的所有质因子判断 i 是否是丑数
//        Set<Integer> set = new HashSet<Integer>();
//        int count = 0;
//        int i = 1;
//        while (count < n) {
//            if (i <= 5) {
//                set.add(i);
//                count++;
//            } else {
//                int sq = (int)Math.sqrt(i);
//                for (int j = 2; j <= sq; j++) {
//                    if (i % j == 0 && set.contains(j) && set.contains(i / j)) {
//                        set.add(i);
//                        count++;
//                        break;
//                    } 
//                }
//            }
//            i++;
//            // System.out.println(set.toString() + " " + count);
//        }
//        return i-1;

        // 方法三：方法二改进（超时）
        // 将每层循环中的丑数判断逻辑改为直接判断针对 2，3，5 的余数判断
        int ret = 1;
        if (n <= 6) {
            return n;
        }
        Set<Integer> set = new HashSet<Integer>();
        for (int i = 1; i <= 6; i++) {
            set.add(i);
        }
        int count = 7;
        int i = 7;
        while (count <= n) {
            boolean isU = true;
            boolean isU2 = false;
            if (i % 2 == 0) {
                isU2 = true;
                if (!set.contains(i / 2)) {
                    isU = false;
                }
            }
            if (i % 3 == 0) { 
                isU2 = true;
                if (!set.contains(i / 3)) {
                    isU = false;
                }
            }
            if (i % 5 == 0) {
                isU2 = true;
                if (!set.contains(i / 5)) {
                    isU = false;
                }
            }
            if (isU && isU2) {
                set.add(i);
                count++;
                ret = i;
            }
            i++;
        }
        return ret;
    }

    public boolean isUglyNumber(int n) {
        if (n <= 5) {
            return true;
        }
        for (int i = 1; i < n; i++) {
            if (n % i == 0 && i != 2 && i!= 3 && i != 5) {
                return false;
            }
        }
        return true;
    }
}

class Ugly1 {
    int[] dp = new int[1960];
    Ugly1() {
        Set<Long> set = new HashSet<Long>();
        PriorityQueue<Long> heap = new PriorityQueue<Long>();
        heap.add(1L);
        set.add(1L);
        for (int i = 0; i < 1960; ++i) {
            long num = heap.poll();
            dp[i] = (int)num;
            long a1 = num * 2, a2 = num * 3, a3 = num * 5;
            if (!set.contains(a1)) {
                heap.add(a1);
                set.add(a1);
            }
            if (!set.contains(a2)) {
                heap.add(a2);
                set.add(a2);
            }
            if (!set.contains(a3)) {
                heap.add(a3);
                set.add(a3);
            }
        }
    }
}

class Solution264_1 {
    public static Ugly1 u = new Ugly1(); // 加了 static 的静态初始化才会让初始化过程只执行一次
    public int nthUglyNumber(int n) {
        // 方法一：堆
        // 利用堆预先计算 1960 内所有的丑数
        return u.dp[n-1];
    }
}

class Ugly2 {
    int[] dp = new int[1690];
    Ugly2() {
        dp[0] = 1;
        int ug, i1 = 0, i2 = 0, i3 = 0;
        for (int i = 1; i < 1690; i++) {
            ug = Math.min(Math.min(dp[i1] * 2, dp[i2] * 3), dp[i3] * 5);
            dp[i] = ug;
            if (ug == dp[i1] * 2) ++i1;
            if (ug == dp[i2] * 3) ++i2;
            if (ug == dp[i3] * 5) ++i3;
        }
    }
}

class Solution264_2 {
    public static Ugly2 ug = new Ugly2();
    public int nthUglyNumber(int n) {
        // 方法二：动态规划（三针针、交错式更新 动态转移方程类型题）
        // 三指针状态转移方程
        return ug.dp[n-1];
    }
}

public class _264_UglyNumber2 {

}
