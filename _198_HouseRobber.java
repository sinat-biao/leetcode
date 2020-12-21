package com.example.leetcode;

import java.util.HashMap;

class Solution198 {
    int ret = 0;
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    public int rob(int[] nums) {
        // 方法一：递归(超时)
        // 每一步都有两种状态：偷或者不偷
//        if (nums.length == 0) {
//            return 0;
//        }
//        robCal(nums, 0, 0, false);
//        robCal(nums, 0, 0, true);
//        return ret;

        // 方法二：动态规划 + Map
        // 状态转移方程：f(n) = max(f(n-2) + nums[n], f(n-1))
        if (nums.length == 0) {
            return 0;
        }
        return robNums(nums, nums.length - 1);
    }

    public int robNums(int[] nums, int j) {
        if (j < 0) {
            return 0;
        }
        int s1 = 0, s2 = 0;
        if (map.containsKey(j-2)) {
            s1 = map.get(j-2);
        } else {
            s1 = robNums(nums, j-2);
            map.put(j-2, s1);
        }
        if (map.containsKey(j-1)) {
            s2 = map.get(j-1);
        } else {
            s2 = robNums(nums, j-1);
            map.put(j-1, s2);
        }
        return Math.max(s1 + nums[j], s2);
    }

    public void robCal(int[] nums, int idx, int sum, boolean isrob) {
        if (idx == nums.length) {
            if (sum > ret) {
                ret = sum;
            }
            return;
        }
        if (isrob) {
            sum += nums[idx];
            robCal(nums, idx+1, sum, false);
        } else {
            robCal(nums, idx+1, sum, true);
            robCal(nums, idx+1, sum, false);
        }
    }
}

public class _198_HouseRobber {

}
