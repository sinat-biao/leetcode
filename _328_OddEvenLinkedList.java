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
class Solution328 {
    public ListNode oddEvenList(ListNode head) {
        // 方法一：双指针
        // 用两个指针分别将原链表拆成奇、偶数链表，然后将偶数链表追加在奇数链表之后即可。
        ListNode i = new ListNode(-1);
        ListNode j = new ListNode(-1);
        ListNode headi = i;
        ListNode headj = j;
        while (head != null) {
            i.next = head;
            i = i.next;
            head = head.next;
            if (head == null) {
                break;
            }
            j.next = head;
            j = j.next;
            head = head.next;
        }
        i.next = headj.next;
        j.next = null;
        return headi.next;
    }
}

public class _328_OddEvenLinkedList {
}
