package com.example.leetcode;

import java.util.HashMap;
import java.util.Map;

class Solution96 {
    public int numTrees(int n) {
        if (n == 0) {
            return 0;
        }
        return generateTreesTools(1, n);
    }

    Map<Pair<Integer, Integer>, Integer> map = new HashMap<Pair<Integer, Integer>, Integer>();

    public int generateTreesTools(int start, int end) {
        int sum = 0;
        // 停止条件
        if (start > end) {
            return 1;
        }
        // 挑选根节点
        for (int i = start; i <= end; i++) {
            int left = 1, right = 1;
            if (map.containsKey(new Pair<>(start, i - 1))) {
                left = map.get(new Pair<>(start, i - 1));
            } else {
                left = generateTreesTools(start, i - 1);
                map.put(new Pair<>(start, i - 1), left);
            }
            if (map.containsKey(new Pair<>(i + 1, end))) {
                right = map.get(new Pair<>(i + 1, end));
            } else {
                right = generateTreesTools(i + 1, end);
                map.put(new Pair<>(i + 1, end), right);
            }
            sum += left * right;
        }
        return sum;
    }
}

public class _96_UniqueBinarySearchTrees {

}
