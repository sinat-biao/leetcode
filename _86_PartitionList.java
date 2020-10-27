package com.leetcode.java;

import java.util.ArrayList;
import java.util.List;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution86 {
    public ListNode partition(ListNode head, int x) {
        // 方法一：数组+2次遍历
        if (head == null) {
            return null;
        }
        ArrayList<ListNode> list1 = new ArrayList<>();
        ArrayList<ListNode> list2 = new ArrayList<>();
        ListNode start = new ListNode(-1);
        while (head != null) {
            if (head.val < x) {
                list1.add(head);
            } else {
                list2.add(head);
            }
            head = head.next;
        }
        head = start;
        for (ListNode l : list1) {
            start.next = l;
            start = start.next;
        }
        for (ListNode l : list2) {
            start.next = l;
            start = start.next;
        }
        start.next = null;
        return head.next;
    }

    public ListNode partition2(ListNode head, int x) {
        // 方法二：双哨兵指针
        // 利用两个哨兵指针分别链接小于 x 的节点和 大于等于 x 的节点。
        ListNode i = new ListNode(-1);
        ListNode j = new ListNode(-1);
        ListNode i_ = i;
        ListNode j_ = j;
        while (head != null) {
            if (head.val < x) {
                i.next = head;
                i = i.next;
            } else {
                j.next = head;
                j = j.next;
            }
            head = head.next;
        }
        i.next = j_.next;
        j.next = null;
        return i_.next;
    }
}

public class _86_PartitionList {
}
