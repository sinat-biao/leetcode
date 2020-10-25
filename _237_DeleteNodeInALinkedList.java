package com.leetcode.java;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution237 {
    public void deleteNode(ListNode node) {
        ListNode pre = null;
        while (node.next != null) {
            pre = node;
            node.val = node.next.val;
            node = node.next;
        }
        pre.next = null;
    }
}

public class _237_DeleteNodeInALinkedList {
    public static void main(String[] args) {
        _237_DeleteNodeInALinkedList deleteNodeInALinkedList = new _237_DeleteNodeInALinkedList();
        int[] list = new int[] {4, 5};
        ListNode head = deleteNodeInALinkedList.test(list);
//        while (head != null) {
//            System.out.print(head.val + " ");
//            head = head.next;
//        }
        Solution237 solution237 = new Solution237();
        solution237.deleteNode(head);
        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
    }

    public ListNode test(int[] list) {
        ListNode start = new ListNode(-1);
        ListNode head = start;
        for (int a : list) {
            start.next = new ListNode(a);
            start = start.next;
        }
        return head.next;
    }
}
