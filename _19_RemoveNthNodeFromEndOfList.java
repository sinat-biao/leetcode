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
class Solution19 {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // 方法一：两次扫描
        // 先扫描一次获得链表的总长度 len，那么要删除的节点从头计数则为第 len - n + 1 个，
        // 其前置节点为第 len - n 个。
        int len = 0;
        ListNode start = head;
        while (start != null) {
            len++;
            start = start.next;
        }
        System.out.println("len = " + len);
        if (len == 1) {
            return null;
        }
        ListNode pre = head;
        int p = len - n;
        if (p > 0) {
            while (p > 1) {
                p--;
                pre = pre.next;
            }
            if (pre.next.next == null) {
                pre.next = null;
            } else {
                pre.next = pre.next.next;
            }
            return head;
        } else {
            return head.next;
        }
    }

    public ListNode removeNthFromEnd2(ListNode head, int n) {
        // 方法二：一次扫描
        // 双指针 i、j，他们之间相隔 n-1 个元素，两者同时向后扫描，当 j 到达末尾时，i 刚好就是倒数第 n 个元素的前一个元素。
        ListNode i = head;
        ListNode j = head;
        int c = n;
        while (c > 0) {
            c--;
            j = j.next;
        }
        if (j == null) {
            return head.next;
        }
        while (j.next != null) {
            i = i.next;
            j = j.next;
        }
        i.next = i.next.next;

        return head;
    }
}

public class _19_RemoveNthNodeFromEndOfList {
}
