package com.example.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution112 {
	
	List<List<Integer>> ret = new ArrayList<List<Integer>>();

    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        // 方法一：深度递归遍历
        if (root == null) {
            return ret;
        }
        paths(root, new ArrayList<Integer>(), sum);
        return ret;
    }

    public void paths(TreeNode root, List<Integer> path, int sum) {
        if (root == null) {
            return;
        }
        if (root.left == null && root.right == null && root.val == sum) {
            path.add(root.val);
            ret.add(List.copyOf(path));
            path.remove(path.size() - 1);
            return;
        }
        if (root.left == null && root.right == null && root.val != sum) {
            return;
        }
        if (root.left != null) {
            path.add(root.val);
            paths(root.left, path, sum - root.val);
            path.remove(path.size() - 1);
        }
        if (root.right != null) {
            path.add(root.val);
            paths(root.right, path, sum - root.val);
            path.remove(path.size() - 1);
        }
    }
}

public class _113_PathSum2 {

}
