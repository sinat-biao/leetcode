package com.example.leetcode;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution110 {
    public boolean isBalanced(TreeNode root) {
        // 方法一：递归的返回左右子树的高度
        if (root == null) {
            return true;
        }
        int leftHeight = 0;
        int rightHeight = 0;
        leftHeight = heightOfTree(root.left);
        rightHeight = heightOfTree(root.right);
        if (Math.abs(leftHeight - rightHeight) > 1) {
            return false;
        } else {
            return isBalanced(root.left) & isBalanced(root.right);
        }
    }

    public int heightOfTree(TreeNode root) {
        int height = 0;
        if (root == null) {
            return height;
        }
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int currentSize = queue.size();
            for (int i = 0; i < currentSize; i++) {
                TreeNode node = queue.poll();
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            height++;
        }
        return height;
    }
}

public class _110_BalancedBinaryTree {

}
