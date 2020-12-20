package com.example.leetcode;

import java.util.HashMap;

class Solution70 {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    int ret = 0;
    public int climbStairs(int n) {
        // ����һ���ݹ飨��ʱ��
        // �ݹ������ÿ���������߷���һ�� or ������
//        if (n < 0) {
//            return 0;
//        }
//        if (n == 0) {
//            ret++;
//            return 0;
//        }
//        // ��һ��
//        climbStairs(n - 1);
//        // ������
//        climbStairs(n - 2);
//        return ret;

        // ����������̬�滮 + Map
        // n ��¥�������ķ����� = n-1 ��¥�������ķ����� + n-2 ��¥�������ķ�����
        // ��̬�滮���̣�f(n) = f(n-1) + f(n-2)
        // ͨ����� Map �ķ�ʽ�洢�Ѿ��������ֵ�������ظ����㵼�µĳ�ʱ
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        int s = 0;
        if (map.containsKey(n-1)) {
            s += map.get(n-1);
        } else {
        	int l = climbStairs(n-1);
        	map.put(n-1, l);
        	s += l;
        }
        if (map.containsKey(n-2)) {
        	s += map.get(n-2);
        } else {
        	int r = climbStairs(n-2);
        	map.put(n-2, r);
        	s += r;
        }
        return s;

        // ����������̬�滮 + �Ե�����
        // �� 0 ��ʼ�ۼӵ��� n ��Ԫ�أ��������ظ�����
//        if (n == 1) {
//            return 1;
//        }
//        if (n == 2) {
//            return 2;
//        }
//        int p = 1, q = 2;
//        int c = 0;
//        for (int i = 3; i <= n; i++) {
//            c = p + q;
//            p = q;
//            q = c;
//        }
//        return c;
    }
}

public class _70_ClimbingStairs {

}
