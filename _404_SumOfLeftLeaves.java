package com.example.leetcode;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution404 {

    int sum = 0;

    public int sumOfLeftLeaves(TreeNode root) {
        // 方法一：递归遍历即可
        if (root == null) {
            return sum;
        }
        if (root.left != null) {
            if (root.left.left == null && root.left.right == null) {
                sum += root.left.val;
            }
            sumOfLeftLeaves(root.left);
        }
        if (root.right != null) {
            sumOfLeftLeaves(root.right);
        }
        return sum;
    }
}

public class _404_SumOfLeftLeaves {

}
