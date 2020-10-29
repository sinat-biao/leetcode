package com.leetcode.java;

import java.util.Stack;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution143 {
    public void reorderList(ListNode head) {
        // 方法一：栈
        Stack<ListNode> stack = new Stack<>();
        ListNode start = head;
        while (start != null) {
            stack.push(start);
            start = start.next;
        }
        start = head;
        while (start != null) {
            ListNode p = stack.pop();
            if (start.next == p) {
                start = start.next;
                break;
            }
            if (start == p) {
                break;
            }
            p.next = start.next;
            start.next = p;
            start = p.next;
        }
        if (start != null) {
            start.next = null;
        }
    }
}

public class _143_ReorderList {
}
