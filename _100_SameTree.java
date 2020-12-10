package com.example.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution100 {
	
	public String serialize(TreeNode root) {
    	// 层次遍历序列化
    	if (root != null) {
    		List<Integer> list = new ArrayList<Integer>();
    		Queue<TreeNode> queue = new LinkedList<TreeNode>();
    		queue.offer(root);
    		while (!queue.isEmpty()) {
    			TreeNode node = queue.poll();
    			if (node == null) {
    				list.add(null);
    				continue;
    			}
    			list.add(node.val);
    			if (node.left != null) {
    				queue.offer(node.left);
    			} else {
    				queue.add(null);
    			}
    			if (node.right != null) {
    				queue.offer(node.right);
    			} else {
    				queue.add(null);
    			}
    		}
    		return list.toString();
    	} else {
    		return "";
    	}
    }
	
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // 方法一：直接序列化，然后比较序列化后的值
//    	String ps = serialize(p);
//        String qs = serialize(q);
//        if (ps.equals(qs)) {
//            return true;
//        }
//        return false;
    	
    	// 方法二：同时递归遍历每个节点
    	if (p == null && q == null) {
            return true;
        } else if (p == null || q == null) {
            return false;
        } else if (p.val != q.val) {
            return false;
        } else {
            return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        }
    }
    
}

public class _100_SameTree {

}
