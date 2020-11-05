package com.leetcode.java;
import java.util.Arrays;
import java.util.HashMap;

class Solution242 {
    public boolean isAnagram(String s, String t) {
        // 方法一：哈希表
        HashMap<Character, Integer> hashSet = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (hashSet.containsKey(s.charAt(i))) {
                hashSet.replace(s.charAt(i), hashSet.get(s.charAt(i))+1);
            } else {
                hashSet.put(s.charAt(i), 1);
            }
        }
        for (int i = 0; i < t.length(); i++) {
            if (hashSet.containsKey(t.charAt(i))) {
                hashSet.replace(t.charAt(i), hashSet.get(t.charAt(i))-1);
                if (hashSet.get(t.charAt(i)) == 0) {
                    hashSet.remove(t.charAt(i));
                }
            } else {
                return false;
            }
        }
        if (hashSet.isEmpty()) {
            return true;
        } else {
            return false;
        }
    }

    public boolean isAnagram2(String s, String t) {
        // 方法二：排序
        char[] charss = s.toCharArray();
        System.out.println(Arrays.toString(charss));
        char[] charst = t.toCharArray();
        System.out.println(Arrays.toString(charst));
        Arrays.sort(charss);
        Arrays.sort(charst);
        System.out.println(Arrays.toString(charss));
        System.out.println(Arrays.toString(charst));
        // 注意，java 中两个数组（除了基本类型和变量）之间的比较，均需要使用 equal 函数
        if (Arrays.equals(charss, charst)) {
            return true;
        } else {
            return false;
        }
    }

    public boolean isAnagram3(String s, String t) {
        // 方法三：哈希表便携实现
        // 使用字符的 ascii 码值代替其自身，然后计数
        if (s.length() != t.length()) {
            return false;
        }
        int[] hashset = new int[26];
        System.out.println(Arrays.toString(hashset));
        for (int i = 0; i < s.length(); i++) {
            hashset[s.charAt(i)-'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            hashset[t.charAt(i)-'a']--;
            if (hashset[t.charAt(i) - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }
}

public class _242_ValidAnagram {
    public static void main(String[] args) {
        Solution242 solution242 = new Solution242();
        String s = "anagram";
        String t = "nagaram";
        System.out.println(solution242.isAnagram3(s, t));
        System.out.println(solution242.isAnagram3("rat", "car"));
    }
}
