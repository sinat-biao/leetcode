package com.leetcode.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

class Solution324 {
    public void wiggleSort(int[] nums) {
        // 方法一：二分数组，间隔插入
        if (nums.length <= 2) {
            Arrays.sort(nums);
        } else {
            Arrays.sort(nums);
            ArrayList<Integer> pre = new ArrayList<>();
            ArrayList<Integer> aft = new ArrayList<>();
            int mid = 0;
            if (nums.length % 2 == 0) {
                mid = nums.length / 2;
            } else {
                mid = nums.length / 2 + 1;
            }
            for (int j = 0; j < mid; j++) {
                pre.add(nums[j]);
            }
            for (int j = mid; j < nums.length; j++) {
                aft.add(nums[j]);
            }
            // 逆序数组
            Collections.reverse(pre);
            Collections.reverse(aft);
            System.out.println(pre.toString() + aft.toString());
            int i = 0;
            int j = 0;
            int k = 0;
            while (k < nums.length) {
                if (i < pre.size() && j < aft.size()) {
                    nums[k++] = pre.get(i++);
                    nums[k++] = aft.get(j++);
                } else {
                    if (i < pre.size()) {
                        nums[k++] = pre.get(i++);
                    } else {
                        nums[k++] = aft.get(j++);
                    }
                }
            }
        }
    }

    public void wiggleSort2(int[] nums) {
        // 方法二：暴力匹配
        if (nums.length <= 2) {
            Arrays.sort(nums);
        } else {
            Arrays.sort(nums);
            int[] nums1 = nums.clone();
            int mid = 0;
            if (nums.length % 2 == 0) {
                mid = nums.length / 2;
            } else {
                mid = nums.length / 2 + 1;
            }
            ArrayList<Integer> pre = new ArrayList<>();
            for (int i = 0; i < mid; i++) {
                pre.add(nums[i]);
            }
            ArrayList<Integer> aft = new ArrayList<>();
            for (int i = mid; i < nums.length; i++) {
                aft.add(nums[i]);
            }
            int insert = 1;
            while (pre.size() < nums.length) {
                if (insert > 0 && nums[mid] > pre.get(insert-1) && nums[mid] > pre.get(insert)) {
                    pre.add(insert, nums[mid++]);
                    insert += 2;
                } else {
                    insert = 0;
                }
            }
            System.out.println("->" + pre.toString());
        }
    }
}

public class _324_WiggleSort2 {
    public static void main(String[] args) {
        Solution324 solution324 = new Solution324();
        int[] nums = new int[]{1, 5, 1, 1, 6, 4};
        solution324.wiggleSort(nums);
        System.out.println(Arrays.toString(nums));
        nums = new int[]{1, 3, 2, 2, 3, 1};
        solution324.wiggleSort(nums);
        System.out.println(Arrays.toString(nums));
        nums = new int[]{4, 5, 5, 6};
        solution324.wiggleSort(nums);
        System.out.println(Arrays.toString(nums));
        nums = new int[]{1, 5, 1, 1, 6, 4};
        solution324.wiggleSort(nums);
        System.out.println(Arrays.toString(nums));
    }
}
