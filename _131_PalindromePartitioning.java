package com.example.leetcode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution131 {
    public List<List<String>> partition(String s) {
        // 方法一：动态规划
        // 从左到右，依次遍历子串可能存在的分割方式，构造缓存 map 
        // map(string[0, i]) = map(string[0, i - 1]) + map(string[0, i - 2])(if string[i-2,i] is palindrome) + ...
        // 边界条件：map(string[0,0]) = [[string[0,0]]]

        Map<String, List<List<String>>> map = new HashMap<String, List<List<String>>>();

        for (int i = 1; i <= s.length(); i++) {
            List<List<String>> ret = new ArrayList<List<String>>();
            Collections.reverse(ret);
            if (i == 1) {
                List<String> lin = new ArrayList<String>();
                String ss = s.substring(0, i);
                lin.add(ss);
                ret.add(lin);
                map.put(ss, ret);
            } else {
                String ss = s.substring(0, i);
                for (int j = i - 1; j >= 0; j--) {
                    String last = ss.substring(j, i);
                    if (isPalindrome(last)) {
                        if (j == 0) {
                            List<String> lin = new ArrayList<String>();
                            lin.add(last);
                            ret.add(lin);
                        } else {
                            for (List<String> ls : map.get(ss.substring(0, j))) {
                                List<String> copy = new ArrayList<String>(ls);
                                copy.add(last);
                                ret.add(copy);
                            }
                        }
                        
                    }
                }
                map.put(ss, ret);
            }
            // System.out.println(map.get(s.substring(0, i)).toString());
        }
        return map.get(s);
    }

    public boolean isPalindrome(String str) {
        int len = str.length();
        int i = 0, j = len - 1;
        while (i < j) {
            if (str.charAt(i) != str.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}

public class _131_PalindromePartitioning {

}
