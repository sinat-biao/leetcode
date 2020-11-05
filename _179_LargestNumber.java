package com.leetcode.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

class Solution179 {
    public String largestNumber(int[] nums) {
        // 方法一：转换成字符串后再排序
        ArrayList<String> arrayList = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            arrayList.add(Integer.toString(nums[i]));
        }
        System.out.println(arrayList.toString());
        arrayList.sort(new Comparator<String>() {
            @Override
            public int compare(String s, String t1) {
                String a = s + t1;
                String b = t1 + s;
                return a.compareTo(b);
            }
        });
        System.out.println(arrayList.toString());
        String string = "";
        for (int k = arrayList.size() - 1; k >= 0; k--) {
            if (string.length() == 0) {
                string = string + arrayList.get(k);
            } else {
                if (string.equals("0") && arrayList.get(k).equals("0")) {
                    continue;
                }
                string = string + arrayList.get(k);
            }
        }
        return string;
    }
}

public class _179_LargestNumber {
    public static void main(String[] args) {
        Solution179 solution179 = new Solution179();
        int[] nums = new int[] {10, 2};
        System.out.println(solution179.largestNumber(nums));
        nums = new int[] {3,30,34,5,9};
        System.out.println(solution179.largestNumber(nums));
        nums = new int[] {34323, 3432};
        System.out.println(solution179.largestNumber(nums));
        nums = new int[] {0,0};
        System.out.println(solution179.largestNumber(nums));
    }
}
