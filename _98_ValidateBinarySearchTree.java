package com.example.leetcode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

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
class Solution98 {
    
    List<Integer> list = new ArrayList<Integer>();

    public boolean isValidBST(TreeNode root) {
        // 方法二：中序遍历
        if (root == null) {
            return true;
        }
        inOrder(root);
        for (int i = 1; i < list.size(); i++) {
            if (list.get(i) <= list.get(i-1)) {
                return false;
            }
        }
        return true;
    }

    public void inOrder(TreeNode root) {
        if (root != null) {
            if (root.left != null) {
                inOrder(root.left);
            }
            list.add(root.val);
            if (root.right != null) {
                inOrder(root.right);
            }
        }
    }
}

public class _98_ValidateBinarySearchTree {

}
