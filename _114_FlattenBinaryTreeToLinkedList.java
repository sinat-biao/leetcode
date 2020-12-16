package com.example.leetcode;

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
class Solution114 {
    public void flatten(TreeNode root) {
        // ����һ���ݹ�
        // �ݹ�Ľ��������ҵ��������������ӽڵ��ϣ�Ȼ���������ٹҵ���������λ����
        if (root != null) {
            if (root.left != null && root.right == null) {
                root.right = root.left;
                root.left = null;
                flatten(root.right);
            } else if (root.left != null && root.right != null) {
                TreeNode l = root.right;
                root.right = root.left;
                root.left = null;
                TreeNode rr = getRRNode(root.right);
                rr.right = l;
                flatten(root.right);
            } else {
                if (root.right != null) {
                    flatten(root.right);
                }
            }
        }
    }

    public TreeNode getRRNode(TreeNode root) {
        // ���������ӽڵ�
        // ǰ����������һ���ڵ�
        TreeNode ret = root;
        if (root.left != null) {
            ret = getRRNode(root.left);
        }
        if (root.right != null) {
            ret = getRRNode(root.right);
        }
        return ret;
    }
}

public class _114_FlattenBinaryTreeToLinkedList {

}
