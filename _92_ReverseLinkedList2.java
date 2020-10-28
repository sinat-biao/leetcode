package com.leetcode.java;

import java.util.Stack;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution92 {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        // 方法一：栈
        // 将 m-n 的节点压入栈中，然后在依次弹出嵌入链表中即可
        Stack<ListNode> stack = new Stack<>();
        int count = 0;
        ListNode start = head;
        ListNode i = head;
        ListNode j = head;
        ListNode pre = new ListNode(-1);
        ListNode pre2 = pre;
        ListNode j_next = null;
        pre.next = head;
        while (count <= n) {
            count++;
            if (count >= m && count <= n) {
                if (count == m) {
                    i = start;
                }
                if (count == n) {
                    j = start;
                    j_next = j.next;
                }
                stack.push(start);
            }
            start = start.next;
            if (count < m) {
                pre = pre.next;
            }
        }
        System.out.println(pre.next.val);
        System.out.println(i.val);
        while (!stack.isEmpty()) {
            ListNode p = stack.pop();
            pre.next = p;
            pre = pre.next;
        }
        pre.next = j_next;
        return pre2.next;
    }
}

public class _92_ReverseLinkedList2 {
}
