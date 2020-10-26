package com.leetcode.java;

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

class Solution2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // 方法一：遍历链表，依次相加
        ListNode head = new ListNode(-1);
        ListNode start = head;
        int jinwei = 0;
        while (l1 != null && l2 != null) {
            head.next = new ListNode(0);
            head = head.next;
            head.val = (l1.val + l2.val + jinwei) % 10;
            jinwei = (l1.val + l2.val + jinwei) / 10;
            l1 = l1.next;
            l2 = l2.next;
        }
        while (l1 != null) {
            head.next = new ListNode(0);
            head = head.next;
            head.val = (l1.val + jinwei) % 10;
            jinwei = (l1.val + jinwei) / 10;
            l1 = l1.next;
        }
        while (l2 != null) {
            head.next = new ListNode(0);
            head = head.next;
            head.val = (l2.val + jinwei) % 10;
            jinwei = (l2.val + jinwei) / 10;
            l2 = l2.next;
        }
        if (jinwei > 0) {
            head.next = new ListNode(jinwei);
            head = head.next;
        }
        head.next = null;
        return start.next;
    }
}

public class _2_AddTwoNumbers {
}
