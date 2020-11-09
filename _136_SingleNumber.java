package com.leetcode.java;

import java.util.HashMap;

class Solution136 {
    public int singleNumber(int[] nums) {
        // 方法一：哈希表
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (hashMap.containsKey(nums[i])) {
                hashMap.put(nums[i], hashMap.get(nums[i])+1);
            } else {
                hashMap.put(nums[i], 1);
            }
        }
        for (Integer key : hashMap.keySet()) {
            if (hashMap.get(key) == 1) {
                return key;
            }
        }
        return 0;
    }

    public int singleNumber2(int[] nums) {
        // 方法二：异或运算
        // 详见官方题解（感觉有一定的特定性）
        int single = 0;
        for (int i : nums) {
            single ^= i;
        }
        return single;
    }
}

public class _136_SingleNumber {
    public static void main(String[] args) {
        Solution136 solution136 = new Solution136();
        int[] nums = new int[] {2,2,1};
        System.out.println(solution136.singleNumber(nums));
        System.out.println(solution136.singleNumber(new int[] {4,1,2,1,2}));
        System.out.println(solution136.singleNumber(new int[] {1}));
        System.out.println(solution136.singleNumber(new int[] {}));
    }
}
