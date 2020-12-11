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
class Solution107 {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
    	// 方法一：层次遍历，逆序插入返回数组即可
    	List<List<Integer>> ret = new ArrayList<List<Integer>>();
    	if (root == null) {
    		return ret;
    	}
    	Queue<TreeNode> queue = new LinkedList<TreeNode>();
    	queue.offer(root);
    	while (!queue.isEmpty()) {
    		int currentSize = queue.size();
    		List<Integer> list = new ArrayList<Integer>();
    		for (int i = 0; i < currentSize; i++) {
    			TreeNode node = queue.poll();
    			list.add(node.val);
    			if (node.left != null) {
    				queue.offer(node.left);
    			}
    			if (node.right != null) {
    				queue.offer(node.right);
    			}
    		}
    		ret.add(0, list);
    	}
    	return ret;
    }
}

public class _107_BinaryTreeLevelOrderTraversal2 {

}
