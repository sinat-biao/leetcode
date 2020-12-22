package com.example.leetcode;

class Solution392 {
    public boolean isSubsequence(String s, String t) {
        // ����һ��˫ָ��
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
    	
        // ����������̬�滮
        int[][] data = new int[t.length() + 1][26];
        // �����һ�и�ֵΪ t �ĳ���
        for (int i = 0; i < 26; i++) {
            data[t.length()][i] = t.length();
        }
        // ��̬�滮����
        // ״̬ת�ƹ�ʽ��
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

        // ���� s
        int tt = 0;
        for (int i = 0; i < s.length(); i++) {
            if (data[tt][s.charAt(i) - 'a'] == t.length()) {
                return false;
            }
            // ��Ҫ����һ����Ѱ��λ���Ƶ� t �ַ�ƥ����ַ�����һ��λ��
            tt = data[tt][s.charAt(i) - 'a'] + 1;
        }
        return true;
    }
}

public class _392_IsSubsequence {

}
