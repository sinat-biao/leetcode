package com.example.leetcode;

import java.util.HashMap;

class Solution70 {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    int ret = 0;
    public int climbStairs(int n) {
        // 方法一：递归（超时）
        // 递归的爬，每次有两种走法（一步 or 两步）
//        if (n < 0) {
//            return 0;
//        }
//        if (n == 0) {
//            ret++;
//            return 0;
//        }
//        // 爬一步
//        climbStairs(n - 1);
//        // 爬两步
//        climbStairs(n - 2);
//        return ret;

        // 方法二：动态规划 + Map
        // n 阶楼梯能爬的方法数 = n-1 阶楼梯能爬的方法数 + n-2 阶楼梯能爬的方法数
        // 动态规划方程：f(n) = f(n-1) + f(n-2)
        // 通过添加 Map 的方式存储已经计算过的值，避免重复计算导致的超时
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        int s = 0;
        if (map.containsKey(n-1)) {
            s += map.get(n-1);
        } else {
        	int l = climbStairs(n-1);
        	map.put(n-1, l);
        	s += l;
        }
        if (map.containsKey(n-2)) {
        	s += map.get(n-2);
        } else {
        	int r = climbStairs(n-2);
        	map.put(n-2, r);
        	s += r;
        }
        return s;

        // 方法三：动态规划 + 自底向上
        // 从 0 开始累加到第 n 个元素，避免了重复计算
//        if (n == 1) {
//            return 1;
//        }
//        if (n == 2) {
//            return 2;
//        }
//        int p = 1, q = 2;
//        int c = 0;
//        for (int i = 3; i <= n; i++) {
//            c = p + q;
//            p = q;
//            q = c;
//        }
//        return c;
    }
}

public class _70_ClimbingStairs {

}
