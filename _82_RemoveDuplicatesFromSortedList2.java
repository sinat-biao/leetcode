package com.leetcode.java;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution82 {
    public ListNode deleteDuplicates(ListNode head) {
        // 方法一：双指针+哨兵
        // 使用两个指针 i、j 来进行重复元素的过滤（[i,j-1] 是重复元素），
        // 并用哨兵节点指向 i 的前一个节点，然后直接将哨兵节点的 next 属性指向 j 即可。
        if (head == null) {
            return null;
        }
        ListNode pre = new ListNode(-1);
        pre.next = head;
        ListNode start = pre;
        ListNode i = head;
        ListNode j = head.next;
        if (j == null) {
            return head;
        }
        while (j != null) {
            if (j.val == i.val) {
                while (j != null && j.val == i.val) {
                    j = j.next;
                }
                pre.next = j;
                i = j;
                if (j == null) {
                    break;
                } else {
                    j = j.next;
                }
            } else {
                i = i.next;
                j = j.next;
                pre = pre.next;
            }
        }
        return start.next;
    }
}

public class _82_RemoveDuplicatesFromSortedList2 {
}
