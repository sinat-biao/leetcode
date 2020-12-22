package com.example.leetcode;

class Solution392 {
    public boolean isSubsequence(String s, String t) {
        // 方法一：双指针
        // int i = 0, j = 0;
        // while (i < s.length() && j < t.length()) {
        //     while (j < t.length() && t.charAt(j) != s.charAt(i)) {
        //         j++;
        //     }
        //     if (j >= t.length()) {
        //         break;
        //     }
        //     i++;
        //     j++;
        // }
        // if (i >= s.length()) {
        //     return true;
        // } else {
        //     return false;
        // }
    	
        // 方法二：动态规划
        int[][] data = new int[t.length() + 1][26];
        // 将最后一行赋值为 t 的长度
        for (int i = 0; i < 26; i++) {
            data[t.length()][i] = t.length();
        }
        // 动态规划缓存
        // 状态转移公式：
        // 1. t[i] == i : data[i][j] = t[i];
        // 2. t[i] != i : data[i][j] = data[i+1][j];
        for (int i = t.length() - 1; i >= 0; i--) {
            for (int j = 0; j < 26; j++) {
                if (t.charAt(i) == 'a' + j) {
                    data[i][j] = i;
                } else {
                    data[i][j] = data[i+1][j];
                }
            }
        }

        // 搜索 s
        int tt = 0;
        for (int i = 0; i < s.length(); i++) {
            if (data[tt][s.charAt(i) - 'a'] == t.length()) {
                return false;
            }
            // 需要将下一个搜寻的位置移到 t 字符匹配的字符的下一个位置
            tt = data[tt][s.charAt(i) - 'a'] + 1;
        }
        return true;
    }
}

public class _392_IsSubsequence {

}
