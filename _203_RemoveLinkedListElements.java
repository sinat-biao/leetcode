package com.leetcode.java;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution203 {
    public ListNode removeElements(ListNode head, int val) {
        while (head != null && head.val == val) {
            head = head.next;
        }
        if (head == null) {
            return null;
        }
        ListNode i = head.next;
        ListNode pre = head;
        while (i != null) {
            if (i.val == val) {
                pre.next = i.next;
            } else {
                pre = pre.next;
            }
            i = i.next;
        }
        return head;
    }
}

public class _203_RemoveLinkedListElements {
}
