package com.example.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

//Definition for a binary tree node.
class TreeNode {
	 int val;
	 TreeNode left;
	 TreeNode right;
	 TreeNode() {}
	 TreeNode(int x) { val = x; }
}

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Codec {

    // Encodes a tree to a single string.
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

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
    	// 层次遍历反序列化
    	if (data.equals("")) {
    		return null;
    	}
    	List<String> list = Arrays.asList(data.substring(1, data.length()-1).split(", "));
//    	System.out.println(list.toString());
    	Queue<String> queue = new LinkedList<String>(list);
    	Queue<TreeNode> queueNode = new LinkedList<TreeNode>();
    	String s = queue.poll();
    	TreeNode root = new TreeNode(Integer.valueOf(s));
    	queueNode.offer(root);
    	while (!queueNode.isEmpty()) {
    		TreeNode node = queueNode.poll();
    		String left = queue.poll();
    		String right = queue.poll();
    		if (!left.equals("null")) {
    			TreeNode leftNode = new TreeNode(Integer.valueOf(left));
    			node.left = leftNode;
    			queueNode.offer(leftNode);
    		}
    		if (!right.equals("null")) {
    			TreeNode rightNode = new TreeNode(Integer.valueOf(right));
    			node.right = rightNode;
    			queueNode.offer(rightNode);
    		}
    	}
		return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));

public class _297_SerializeAndDeserializeBinaryTree {
	
	public static void main(String[] args) {
		Codec codec = new Codec();
		
		TreeNode root = new TreeNode(1);
		TreeNode l1 = new TreeNode(2);
		TreeNode l2 = new TreeNode(3);
		root.left = l1;
		root.right = l2;
		TreeNode l3 = new TreeNode(4);
		TreeNode l4 = new TreeNode(5);
		l2.left = l3;
		l2.right = l4;	
		String serializeString = codec.serialize(root);
		System.out.println(serializeString);
		TreeNode r = codec.deserialize(serializeString);
		System.out.println(codec.serialize(r));
	}

}
