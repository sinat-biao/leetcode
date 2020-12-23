package com.example.leetcode;

import java.util.HashMap;
import java.util.Map;

class Solution91 {
    private Map<String, Integer> map = new HashMap<String, Integer>();
    public int numDecodings(String s) {
        // 方法一：动态规划
        // 构造一个 HashMap 用于缓存当前字符串（索引从 0 到 i）的组合数
        // 则字符串 s[j](j代表字符个数) 的组合数为 numDecodings(s[0, j-2]) + numDecodings(s[j-2, j]) - 1 (先在 hashmap 中搜索，如果没有，就递归计算并添加到 hashmap 中)
        // 边界条件：

        if (s.contains("00")) {
            return 0;
        }
        if (s.length() == 0) {
            return 0;
        }
        if (s.charAt(0) == '0') {
            return 0;
        }
        if (s.length() == 1) {
            return 1;
        } 
        if (s.length() == 2) {
            if (Integer.valueOf(s) > 26) {
                if (s.charAt(1) == '0') {
                    return 0;
                } else {
                    return 1;
                }
            } else {
                if (s.charAt(1) == '0') {
                    return 1;
                } else {
                    return 2;
                }
            }
        }
        int i = s.length() - 2;
        String pre2 = s.substring(0, i);
        String pre1 = s.substring(0, i + 1);
        String last2 = s.substring(i, s.length());
        String last1 = s.substring(i + 1, s.length());
        if (last2.charAt(0) == '0') {
            if (map.containsKey(pre1)) {
                return map.get(pre1);
            } else {
                int val = numDecodings(pre1);
                map.put(pre1, val);
                return val;
            }
        } else if (Integer.valueOf(last2) <= 26) {
            if (last2.charAt(1) == '0') {
                if (map.containsKey(pre2)) {
                    return map.get(pre2);
                } else {
                    int val = numDecodings(pre2);
                    map.put(pre2, val);
                    return val;
                }
            } else {
                int v1 = 0;
                int v2 = 0;
                if (map.containsKey(pre2)) {
                    v1 = map.get(pre2);
                } else {
                    v1 = numDecodings(pre2);
                    map.put(pre2, v1);
                }
                if (map.containsKey(pre1)) {
                    v2 = map.get(pre1);
                } else {
                    v2 = numDecodings(pre1);
                    map.put(pre1, v2);
                }
                return v1 + v2;
            }
        } else {
            if (last2.charAt(1) == '0') {
                return 0;
            } else {
                // 注意这里大于 26 时，例如 34， 其 3 还是可以分给前面字符串，可能会有其余的组合形式出现
                if (map.containsKey(pre1)) {
                    return map.get(pre1);
                } else {
                    int val = numDecodings(pre1);
                    map.put(pre1, val);
                    return val;
                }
            }
        }
    }
}

public class _91_DecodeWays {

}
