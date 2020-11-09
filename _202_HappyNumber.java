package com.leetcode.java;

import java.util.HashMap;
import java.util.HashSet;

class Solution202 {
    public boolean isHappy(int n) {
        // 方法一：哈希表
        // 利用哈希表判断是否发生无限循环
        String string = String.valueOf(n);
        HashSet<Integer> hashSet = new HashSet<>();
        hashSet.add(n);
        while (true) {
            int new_num = 0;
            for (char c : string.toCharArray()) {
                new_num += (c-'0') * (c-'0');
            }
            if (new_num == 1) {
                return true;
            }
            if (hashSet.contains(new_num)) {
                return false;
            } else {
                hashSet.add(new_num);
            }
            string = String.valueOf(new_num);
            System.out.println(hashSet.toString());
        }
    }

    public boolean isHappy2(int n) {
        // 方法二：快慢指针
        // 使用两个指针来计数当前的数，若不存在循环，则快指针将先达到 1；
        // 若存在循环，则快慢指针将会在某个时刻相遇。
        String stringi = String.valueOf(n);
        String stringj = String.valueOf(n);
        int i = n;
        int j = n;
        while (true) {
            for (int k = 0; k < 2; k++) {
                i = 0;
                for (char c : stringi.toCharArray()) {
                    i += (c - '0') * (c - '0');
                }
                if (i == 1) {
                    return true;
                }
                if (i == j) {
                    return false;
                }
                stringi = String.valueOf(i);
            }
            j = 0;
            for (char c : stringj.toCharArray()) {
                j += (c - '0') * (c - '0');
            }
            stringj = String.valueOf(j);
        }
    }
}

public class _202_HappyNumber {
    public static void main(String[] args) {
        Solution202 solution202 = new Solution202();
        System.out.println(solution202.isHappy2(19));
        System.out.println(solution202.isHappy2(2));
    }
}
