package com.example.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution257 {
    
	List<String> ret = new ArrayList<String>();

    public List<String> binaryTreePaths(TreeNode root) {
        // 方法一：深度递归遍历
        // 每次遍历到叶子节点就将当前路径加入 ret
        if (root == null) {
            return ret;
        }
        List<Integer> path = new ArrayList<Integer>();
        // path.add(root.val);
        deepSearch(root, path);
        return ret;
    }

    public void deepSearch(TreeNode root, List<Integer> path) {
        path.add(root.val);
        if (root.left == null && root.right == null) {
            String s = "";
            for (Integer i : path) {
                s = s + i + "->";
            }
            ret.add(s.substring(0, s.length() - 2));
            path.remove(path.size()-1);
            return;
        }
        if (root.left != null) {
            deepSearch(root.left, path);
        }
        if (root.right != null) {
            deepSearch(root.right, path);
        }
        path.remove(path.size()-1);
    }
}

public class _257_BinaryTreePaths {

}
