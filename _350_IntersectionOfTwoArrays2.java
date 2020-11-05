package com.leetcode.java;

import java.util.ArrayList;
import java.util.Arrays;

class Solution350 {
    public int[] intersect(int[] nums1, int[] nums2) {
        // 方法一：排序+双指针
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        ArrayList arrayList = new ArrayList();
        int i = 0;
        int j = 0;
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] == nums2[j]) {
                arrayList.add(nums1[i]);
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
        for (int c = 0; c < arrayList.size(); c++) {
            re[c] = (int)arrayList.get(c);
        }
        return re;
    }
}

public class _350_IntersectionOfTwoArrays2 {
    public static void main(String[] args) {
        Solution350 solution350 = new Solution350();
        int[] nums1 = new int[] {1,2,2,1};
        int[] nums2 = new int[] {2,2};
        System.out.println(Arrays.toString(solution350.intersect(nums1, nums2)));
        nums1 = new int[]{4, 9, 5};
        nums2 = new int[] {9,4,9,8,4};
        System.out.println(Arrays.toString(solution350.intersect(nums1, nums2)));
    }
}
