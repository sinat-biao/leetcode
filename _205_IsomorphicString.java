package com.leetcode.java;

import java.util.HashMap;

class Solution205 {
    public boolean isIsomorphic(String s, String t) {
        // 方法一：hashmap
        HashMap<Character, Character> hashMap = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (hashMap.containsKey(s.charAt(i))) {
                if (hashMap.get(s.charAt(i)) != t.charAt(i)) {
                    return false;
                }
            } else {
                hashMap.put(s.charAt(i), t.charAt(i));
            }
        }
        hashMap.clear();
        for (int i = 0; i < t.length(); i++) {
            if (hashMap.containsKey(t.charAt(i))) {
                if (hashMap.get((t.charAt(i))) != s.charAt(i)) {
                    return false;
                }
            } else {
                hashMap.put(t.charAt(i), s.charAt(i));
            }
        }
        return true;
    }
}

public class _205_IsomorphicString {
    public static void main(String[] args) {
        Solution205 solution205 = new Solution205();
        System.out.println(solution205.isIsomorphic("egg", "add"));
        System.out.println(solution205.isIsomorphic("foo", "bar"));
        System.out.println(solution205.isIsomorphic("paper", "title"));
        System.out.println(solution205.isIsomorphic("ab", "aa"));
    }
}
