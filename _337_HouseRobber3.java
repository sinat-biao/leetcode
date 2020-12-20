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
class Solution337 {

    int retsum = 0;

    public int rob(TreeNode root) {
        // 方法一：深度递归
        // 深度递归，在此过程中求和
        if (root == null) {
            return 0;
        }
        preOrderAndSum(root, 0, true);
        preOrderAndSum(root, 0, false);
        return retsum;
    }

    public int preOrderAndSum(TreeNode root, int sum, boolean curis) {
        if (curis) {
            sum += root.val;
        }
        if (sum > retsum) {
            retsum = sum;
        }
        if (root.left != null) {
            if (curis) {
                sum = preOrderAndSum(root.left, sum, false);
            } else {
                int sum1 = preOrderAndSum(root.left, sum, false);
                int sum2 = preOrderAndSum(root.left, sum, true);
                if (sum1 > sum2) {
                    sum = sum1;
                } else {
                    sum = sum2;
                }
            }
        }
        if (root.right != null) {
            if (curis) {
                sum = preOrderAndSum(root.right, sum, false);
            } else {
                int sum1 = preOrderAndSum(root.right, sum, false);
                int sum2 = preOrderAndSum(root.right, sum, true);
                if (sum1 > sum2) {
                    sum = sum1;
                } else {
                    sum = sum2;
                }
            }
        }
        if (sum > retsum) {
            retsum = sum;
        }
        return sum;
    }
}

public class _337_HouseRobber3 {

}
