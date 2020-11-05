package com.leetcode.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

class Solution349 {
    public int[] intersection(int[] nums1, int[] nums2) {
        // 方法一：排序+合并
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int i = 0;
        int j = 0;
        ArrayList<Integer> arrayList = new ArrayList<>();
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] == nums2[j]) {
                if (!arrayList.contains(nums1[i])) {
                    arrayList.add(nums1[i]);
                }
                i++;
                j++;
            } else {
                if (nums1[i] < nums2[j]) {
                    i++;
                } else {
                    j++;
                }
            }
        }
        int[] re = new int[arrayList.size()];
        int count = 0;
        for (Integer a : arrayList) {
            re[count++] = a;
        }
        return re;
    }

    public int[] intersection2(int[] nums1, int[] nums2) {
        // 方法二：哈希表
        HashSet<Integer> hashSet1 = new HashSet<Integer>();
        HashSet<Integer> hashSet2 = new HashSet<>();
        for (int i = 0; i < nums1.length; i++) {
            hashSet1.add(nums1[i]);
        }
        for (int i = 0; i < nums2.length; i++) {
            hashSet2.add(nums2[i]);
        }
        List<Integer> arrays = new ArrayList<Integer>();
        for (Integer s : hashSet1) {
            if (hashSet2.contains(s)) {
                arrays.add(s);
            }
        }
        int[] re = new int[arrays.size()];
        for (int i = 0; i < arrays.size(); i++) {
            re[i] = arrays.get(i);
        }
        return re;
    }
}

public class _349_IntersectionOfTwoArrays {
    public static void main(String[] args) {
        Solution349 solution349 = new Solution349();
        int[] nums1 = new int[] {1, 2, 2, 1};
        int[] nums2 = new int[] {2, 2};
        System.out.println(Arrays.toString(solution349.intersection2(nums1, nums2)));
        System.out.println(Arrays.toString(solution349.intersection2(new int[] {4,9,5}, new int[] {9,4,9,8,4})));
    }
}
