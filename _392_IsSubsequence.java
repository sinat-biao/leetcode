package com.leetcode.java;

import java.util.HashSet;

class Solution392 {
    public boolean isSubsequence(String s, String t) {
        int j = 0;
        for (int i = 0; i < s.length(); i++) {
            while (j < t.length() && t.charAt(j) != s.charAt(i)) {
                j++;
            }
            if (j < t.length()) {
                System.out.print(j + " " + t.charAt(j) + "\n");
            }
            if (j == t.length()) {
                return false;
            }
            j++;
        }
        return true;
    }

    public boolean isSubsequence2(String s, String t) {
        // 方法二：双指针一次遍历
        int i = 0;
        int j = 0;
        while (j < t.length()) {
            if (t.charAt(j) != s.charAt(i)) {
                j++;
            } else {
                i++;
                j++;
            }
        }
        if (i == s.length()) {
            return true;
        } else {
            return false;
        }
    }
}

public class _392_IsSubsequence {
    public static void main(String[] args) {
        Solution392 solution392 = new Solution392();
        System.out.println(solution392.isSubsequence2("abc", "ahbgdc"));
        System.out.println(solution392.isSubsequence2("axc", "ahbgdc"));
        System.out.println(solution392.isSubsequence2("axc", "ahbgdx"));
    }
}
