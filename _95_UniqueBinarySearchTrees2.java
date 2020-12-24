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
        // ����һ���ݹ��Ͷ�̬�滮
        if (n == 0) {
            return new ArrayList<TreeNode>();
        }
        return generateTreesTools(1, n);
    }

    public List<TreeNode> generateTreesTools(int start, int end) {
        List<TreeNode> all = new ArrayList<TreeNode>();
        // ֹͣ����
        if (start > end) {
            // System.out.println(all);
            all.add(null);  // ����Ӹ� null ��Ŀ������ʹ�ú�����ڵ�ȡ��������ʱ��ֱ��ȡ������ null����������Ϊ all Ϊ�ն�ȡ����ֵ������ѭ������������һ������������ֵȴ�޷�ƴ��
            // System.out.println(all);
            return all;
        }
        // ��ѡ���ڵ�
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
