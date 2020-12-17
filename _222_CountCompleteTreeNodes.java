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
class Solution222 {

    int count = 0;

    public int countNodes(TreeNode root) {
        // ����һ������������ͳ�����нڵ���
        preOrder(root);
        return count;
    }

    public void preOrder(TreeNode root) {
        if (root != null) {
            count++;
            if (root.left != null) {
                preOrder(root.left);
            }
            if (root.right != null) {
                preOrder(root.right);
            }
        }
    }
}

public class _222_CountCompleteTreeNodes {

}
