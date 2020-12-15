package com.example.leetcode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution103 {

    Queue<TreeNode> queue = new LinkedList<TreeNode>();

    boolean s = false;
    
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
    	// 方法一：层次遍历
        // 添加逆反参数 s 来决定每一层遍历后是否需要逆序
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        if (root == null) {
            return ret;
        }
        queue.offer(root);
        while (!queue.isEmpty()) {
            int currentLevelSize = queue.size();
            List<Integer> list = new ArrayList<Integer>();
            for (int i = 0; i < currentLevelSize; i++) {
                TreeNode node = queue.poll();
                if (s) {
                    list.add(0, node.val);
                } else {
                    list.add(node.val);
                }
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            ret.add(list);
            s = !s;
        }
        return ret;
    }
}

public class _103_BinaryTreeZigzagLevelOrderTraversal {

}
