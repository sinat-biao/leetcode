package com.example.leetcode;

class Solution5 {
    public String longestPalindrome(String s) {
        // ����һ��˫ָ����չ
        // ͬʱΪ����ż���޷��Գ���չ����ԭ�ַ����м���Ĳ���ָ���
        // String ret = "";
        // String s2 = "";
        // for (int i = 0; i < s.length(); i++) {
        //     s2 += "#" + s.charAt(i);
        // }
        // s2 += "#";
        // s = s2;
        // for (int i = 0; i < s.length(); i++) {
        //     if (i == 0) {
        //         ret = s.charAt(i) + "";
        //         continue;
        //     }
        //     int pre = i, net = i;
        //     while (pre >= 0 && net < s.length() && s.charAt(pre) == s.charAt(net)) {
        //         pre--;
        //         net++;
        //     }
        //     if (net - pre + 1 > ret.length()) {
        //         ret = s.substring(pre+1, net);
        //     }
        // }
        // return ret.replace("#", "");

        // ����������̬�滮
        // ����һ��״̬���� dp[][] ��dp[i][j] ��ʾ �� i ~ j ���Ӵ��Ƿ��ǻ��Ĵ�
        // ��ô dp[i][j] = dp[i+1][j-1] & s[i] == s[j]
        // �߽�������
        // 1. �����ַ���dp[i][j] = true
        // 2. �����ַ���dp[i][j] = s[i] == s[j]
        boolean[][] dp = new boolean[s.length()][s.length()];
        String ret = "";
        // ���˳��μ���ѡ���
        for (int j = 0; j < s.length(); j++) {
            for (int i = 0; i <= j; i++) {
                if (j == i) {
                    dp[i][j] = true;
                } else if (j == i + 1) {
                    dp[i][j] = (s.charAt(i) == s.charAt(j));
                } else {
                    dp[i][j] = dp[i+1][j-1] && (s.charAt(i) == s.charAt(j));
                }
                if (dp[i][j] && j - i + 1 >= ret.length()) {
                    ret = s.substring(i, j+1);
                }
            }
        }
        return ret;
    }
}

public class _5_LongestPalindromicSubstring {

}
