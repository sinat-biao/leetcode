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
class Solution {
    public ListNode swapPairs(ListNode head) {
        // 方法一：双指针+哨兵节点
        ListNode s = new ListNode(-1);
        s.next = head;
        if (head == null) {
            return null;
        }
        ListNode i = head;
        ListNode j = head;
        j = j.next;
        if (j == null) {
            return head;
        }
        // 首先交换开头的两个节点
        s.next = j;
        i.next = j.next;
        j.next = i;
        ListNode pre = i;
        i = i.next;
        if (i == null) {
            return s.next;
        }
        j = i.next;
        // 交换剩下的节点
        while (j != null) {
            pre.next = j;
            i.next = j.next;
            j.next = i;
            pre = i;
            i = i.next;
            if (i == null) {
                break;
            }
            j = i.next;
        }
        return s.next;
    }
}

public class _24_SwapNodesInPairs {
}
