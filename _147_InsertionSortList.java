package com.leetcode.java;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution147 {
    public ListNode insertionSortList(ListNode head) {
        // 方法一：随便实现
        if (head == null) {
            return null;
        }
        ListNode pre = new ListNode(-1);
        pre.next = head;
        ListNode p = head.next;
        ListNode i = pre;
        head.next = null;
        while (p != null) {
            while (i.next != null && i.next.val < p.val) {
                i = i.next;
            }
            ListNode pc = p.next;
            p.next = null;
            p.next = i.next;
            i.next = p;
            p = pc;
            i = pre;
        }
        return pre.next;
    }
}

public class _147_InsertionSortList {
}
