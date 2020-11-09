package com.leetcode.java;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.TreeSet;

class Solution220 {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        // 方法一：暴力搜索（超时）
        int len = nums.length;
        int i = 0;
        int j = 0;
        if (k >= len) {
            j = len - 1;
        } else {
            j = i + k;
        }
        while (i < len && j < len) {
            for (int i_ = i; i_ < j; i_++) {
                for (int j_ = i_ + 1; j_ <= j; j_++) {
                    if (Math.abs((long)nums[i_] - (long)nums[j_]) <= t) {
                        return true;
                    }
                }
            }
            i++;
            j++;
        }
        return false;
    }

    public boolean containsNearbyAlmostDuplicate2(int[] nums, int k, int t) {
        // 方法二：滑动窗口+哈希
        // 在 i-j 窗口滑动时，每次后移一个元素时，只有最后一元素是新的，只有最前一个元素被挤出，
        // 所以 hashset 不用全部清空，只需要把被挤出的元素删掉，并判断新入元素即可
        if (nums.length == 0) {
            return false;
        }
        if (k >= nums.length) {
            k = nums.length - 1;
        }
        HashSet<Long> hashSet = new HashSet<>();
        for (int i = 0; i <= k; i++) {
            if (hashSet.contains((long)nums[i])) {
                return true;
            } else {
                if (Math.abs(t) < nums.length) {
                    for (int j = -t; j <= t; j++) {
                        if (hashSet.contains((long)nums[i] + (long)j)) {
                            return true;
                        }
                    }
                } else {
                    for (Long h : hashSet) {
                        if (Math.abs(h - (long)nums[i]) <= t) {
                            return true;
                        }
                    }
                }

                hashSet.add((long)nums[i]);
            }
        }
        hashSet.remove((long)nums[0]);
        for (int i = k + 1; i < nums.length; i++) {
            if (hashSet.contains((long)nums[i])) {
                return true;
            } else {
                if (Math.abs(t) < nums.length) {
                    for (int j = -t; j <= t; j++) {
                        if (hashSet.contains((long)nums[i] + (long)j)) {
                            return true;
                        }
                    }
                } else {
                    for (Long h : hashSet) {
                        if (Math.abs(h - (long)nums[i]) <= t) {
                            return true;
                        }
                    }
                }
                hashSet.add((long)nums[i]);
            }
            hashSet.remove((long)nums[i-k]);
        }
        return false;
    }

    public boolean containsNearbyAlmostDuplicate3(int[] nums, int k, int t) {
        // 方法三：自平衡二叉树
        // 详见题解：https://leetcode-cn.com/problems/contains-duplicate-iii/solution/cun-zai-zhong-fu-yuan-su-iii-by-leetcode/
        // 这里主要是利用了自平衡二叉树能在 O(logn) 的时间内完成插入、搜索、删除操作，
        // 且自平衡二叉树能很容易的搜索大于等于（或小于等于）指定元素的最小元素。
        TreeSet<Long> set = new TreeSet<>();
        for (int i = 0; i < nums.length; i++) {
            Long s = set.ceiling((long)nums[i]);
            if (s != null && s - (long)nums[i] <= (long)t) {
                return true;
            }
            Long g = set.floor((long)nums[i]);
            if (g != null && (long)nums[i] - g <= (long)t) {
                return true;
            }
            set.add((long)nums[i]);
            if (set.size() > k) {
                set.remove((long)nums[i-k]);
            }
        }
        return false;
    }

    public boolean containsNearbyAlmostDuplicate4(int[] nums, int k, int t) {
        // 方法四：桶排序
        Map<Long, Long> d = new HashMap<>();
        long w = (long)t + 1;
        for (int i = 0; i < nums.length; i++) {
            long m = getID(nums[i], w);
            // 检查同一个桶中是否有重复元素
            if (d.containsKey(m)) {
                return true;
            }
            // 检查相邻桶中是否有满足条件的元素
            if (d.containsKey(m-1) && Math.abs(d.get(m-1) - (long)nums[i]) < w) {
                return true;
            }
            if (d.containsKey(m+1) && Math.abs(d.get(m+1) - nums[i]) < w) {
                return true;
            }
            d.put(m, (long)nums[i]);
            if (i >= k) {
                d.remove(getID(nums[i-k], w));
            }
        }
        return false;
    }

    private long getID(long x, long w) {
        // 返回桶的编号
        // x 代表当前元素，w 代表每个桶中存储的数据范围的个数（注意范围为 0-t 时，个数为 t+1）
        // In Java, `-3 / 5 = 0` and but we need `-3 / 5 = -1`
        return x >= 0 ? x / w : (x+1) / w - 1;
    }
}

public class _220_ContainsDuplicate3 {
    public static void main(String[] args) {
        Solution220 solution220 = new Solution220();
        int[] nums = new int[] {1,2,3,1};
        int k = 3, t = 0;
        System.out.println(solution220.containsNearbyAlmostDuplicate3(
                nums, k, t
        ));     // true
        System.out.println(solution220.containsNearbyAlmostDuplicate3(
                new int[] {1,0,1,1}, 1, 2
        ));     // true
        System.out.println(solution220.containsNearbyAlmostDuplicate3(
                new int[] {1,5,9,1,5,9}, k = 1, t = 2
        ));     // false
        System.out.println(solution220.containsNearbyAlmostDuplicate3(
                new int[] {-2147483648,2147483647}, k = 1, t = 1
        ));     // false
        System.out.println(solution220.containsNearbyAlmostDuplicate3(
                new int[] {2147483646,2147483647}, k = 3, t = 3
        ));     // true
        System.out.println(solution220.containsNearbyAlmostDuplicate3(
                new int[] {8,7,15,1,6,1,9,15}, k = 1, t = 3
        ));     // true
    }
}
