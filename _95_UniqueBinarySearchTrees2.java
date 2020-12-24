package com.example.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
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
class Solution95 {
    public List<TreeNode> generateTrees(int n) {
        // 方法一：递归型动态规划
        if (n == 0) {
            return new ArrayList<TreeNode>();
        }
        return generateTreesTools(1, n);
    }

    public List<TreeNode> generateTreesTools(int start, int end) {
        List<TreeNode> all = new ArrayList<TreeNode>();
        // 停止条件
        if (start > end) {
            // System.out.println(all);
            all.add(null);  // 这里加个 null 的目的在于使得后面根节点取左右子树时，直接取出的是 null，而不会因为 all 为空而取不到值，导致循环结束，另外一个子树尽管有值却无法拼接
            // System.out.println(all);
            return all;
        }
        // 挑选根节点
        for (int i = start; i <= end; i++) {
            List<TreeNode> left = generateTreesTools(start, i - 1);
            List<TreeNode> right = generateTreesTools(i + 1, end);
            for (TreeNode l : left) {
                for (TreeNode r : right) {
                    TreeNode root = new TreeNode(i);
                    root.left = l;
                    root.right = r;
                    all.add(root);
                }
            }
        }
        return all;
    }
}

public class _95_UniqueBinarySearchTrees2 {

}
