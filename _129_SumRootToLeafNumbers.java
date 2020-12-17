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
class Solution129 {

    public int sum = 0;

    public int sumNumbers(TreeNode root) {
        preOrder(root, 0);
        return sum;
    }

    List<Integer> pathList = new ArrayList<Integer>();

    public void preOrder(TreeNode root, int pathSum) {
        if (root != null) {
            if (root.left == null && root.right == null) {
                pathSum = pathSum * 10 + root.val;
                sum += pathSum;
                pathSum = pathSum / 10;
                return;
            }
            if (root.left != null) {
                preOrder(root.left, pathSum * 10 + root.val);
            }
            if (root.right != null) {
                preOrder(root.right, pathSum * 10 + root.val);
            }
        }
    }
}

public class _129_SumRootToLeafNumbers {

}
