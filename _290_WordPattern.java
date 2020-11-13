package com.leetcode.java;

import java.util.Arrays;
import java.util.HashMap;

class Solution290 {
    public boolean wordPattern(String pattern, String s) {
        // 方法一：哈希表
        String[] sp = s.split(" ");
        if (pattern.length() != sp.length) {
            return false;
        }
        HashMap<Character, String> hashMap = new HashMap<>();
        System.out.println(Arrays.toString(sp));
        for (int i = 0; i < pattern.length(); i++) {
            if (hashMap.containsKey(pattern.charAt(i))) {
                if (!hashMap.get(pattern.charAt(i)).equals(sp[i])) {
                    return false;
                }
            } else {
                if (hashMap.containsValue(sp[i])) {
                    return false;
                } else {
                    hashMap.put(pattern.charAt(i), sp[i]);
                }
            }
        }
        return true;
    }
}

public class _290_WordPattern {
    public static void main(String[] args) {
        Solution290 solution290 = new Solution290();
        System.out.println(solution290.wordPattern("abba", "dog cat cat dog"));
        System.out.println(solution290.wordPattern("abba", "dog cat cat fish"));
        System.out.println(solution290.wordPattern("aaaa", "dog cat cat dog"));
        System.out.println(solution290.wordPattern("abba", "dog dog dog dog"));
        System.out.println(solution290.wordPattern("aaa", "dog dog dog"));
    }
}
