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
class BSTIterator {

    Queue<Integer> queue = new LinkedList<Integer>();

    public void inOrder(TreeNode root) {
        // ÖÐÐò±éÀú
        if (root != null) {
            if (root.left != null) {
                inOrder(root.left);
            }
            queue.offer(root.val);
            if (root.right != null) {
                inOrder(root.right);
            }
        }
    }

    public BSTIterator(TreeNode root) {
        inOrder(root);
    }
    
    public int next() {
        return queue.poll();
    }
    
    public boolean hasNext() {
        if (!queue.isEmpty()) {
            return true;
        } else {
            return false;
        }
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */

public class _173_BinarySearchTreeIterator {

}
