package com.leetcode.java;

import java.util.Stack;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution206 {
    public ListNode reverseList(ListNode head) {
        // 方法一：用栈模拟递归
        if (head == null) {
            return null;
        }
        Stack<ListNode> stack = new Stack<>();
        while (head != null) {
            stack.push(head);
            head = head.next;
        }
        ListNode start = null;
        if (!stack.isEmpty()) {
            head = stack.pop();
            start = head;
        }
        while (!stack.isEmpty()) {
            head.next = stack.pop();
            head = head.next;
        }
        head.next = null;
        return start;
    }

    public ListNode reverseList2(ListNode head) {
        // 方法二：顺序更改指针
        if (head == null) {
            return null;
        }
        ListNode i = head;
        ListNode j = head;
        ListNode pre = null;
        while (j.next != null) {
            pre = j;
            j = j.next;
        }
        System.out.println("prev.val = " + pre.val);
        System.out.println("j.val = " + j.val);
        pre.next = null;
        ListNode end = j;
        while (head != null) {
            while (i.next != null) {
                pre = i;
                i = i.next;
            }
            j.next = i;
            j = j.next;
            if (head.next != null) {
                pre.next = null;
                i = head;
            } else {
                j.next = null;
                head = null;
            }
        }
        return end;
    }
}

public class _206_ReverseLinkedList {
    public static void main(String[] args) {
        _206_ReverseLinkedList reverseLinkedList = new _206_ReverseLinkedList();
        int[] list = new int[] {1, 2, 3, 4, 5};
        ListNode head = reverseLinkedList.test(list);
//        while (head != null) {
//            System.out.print(head.val + " ");
//            head = head.next;
//        }
        Solution206 solution206 = new Solution206();
        ListNode rev = solution206.reverseList2(head);
        while (rev != null) {
            System.out.print(rev.val + " ");
            rev = rev.next;
        }
    }

    public ListNode test(int[] list) {
        ListNode head = new ListNode(-1);
        ListNode st = head;
        for (int a : list) {
            head.next = new ListNode(a);
            head = head.next;
        }
        return st.next;
    }
}
