package com.leetcode.java;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution61 {
    public ListNode rotateRight(ListNode head, int k) {
        // 方法一：循环修改尾节点
        // 这里要注意的一点是要避免超时，所有需要先计算链表长度，计算最小的循环次数。
        ListNode end = head;
        if (head == null || head.next == null) {
            return head;
        }
        int len = 0;
        while (end != null) {
            end = end.next;
            len++;
        }
        System.out.println("len = " + len);
        end = head;
        k = k % len;
        for (int i = 0; i < k; i++) {
            while (end.next != null) {
                end = end.next;
            }
            end.next = head;
            head = end;
            ListNode pre = end;
            while (pre.next != end) {
                pre = pre.next;
            }
            pre.next = null;
        }
        return head;
    }

    public ListNode rotateRight2(ListNode head, int k) {
        // 方法二：双指针
        ListNode i = head;
        ListNode j = head;
        if (head == null || head.next == null) {
            return head;
        }
        int len = 0;
        while (j.next != null) {
            len++;
            j = j.next;
        }
        len++;
        k = k % len;
        if (k == 0) {
            return head;
        }
        for (int p = 0; p < len - k - 1; p++) {
            i = i.next;
        }
        j.next = head;
        head = i.next;
        i.next = null;
        return head;
    }
}

public class _61_RotateList {
}
