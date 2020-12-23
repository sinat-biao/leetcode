package com.example.leetcode;

import java.util.HashMap;
import java.util.Map;

class Solution91 {
    private Map<String, Integer> map = new HashMap<String, Integer>();
    public int numDecodings(String s) {
        // ����һ����̬�滮
        // ����һ�� HashMap ���ڻ��浱ǰ�ַ����������� 0 �� i���������
        // ���ַ��� s[j](j�����ַ�����) �������Ϊ numDecodings(s[0, j-2]) + numDecodings(s[j-2, j]) - 1 (���� hashmap �����������û�У��͵ݹ���㲢��ӵ� hashmap ��)
        // �߽�������

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
                // ע��������� 26 ʱ������ 34�� �� 3 ���ǿ��Էָ�ǰ���ַ��������ܻ�������������ʽ����
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
