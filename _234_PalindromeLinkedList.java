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
class Solution234 {
    public boolean isPalindrome(ListNode head) {
        // 方法一：用栈
        Stack<ListNode> stack = new Stack<>();
        ListNode start = head;
        while (head != null) {
            stack.push(head);
            head = head.next;
        }
        while (start != null) {
            if (start.val != stack.pop().val) {
                return false;
            }
            start = start.next;
        }
        return true;
    }

    public boolean isPalindrome2(ListNode head) {
        // 方法二：双指针
        // 用两个指针 i、j，j 首先遍历到末尾，统计节点总个数，然后即可得到中间节点的位置。
        // 然后反转后半部分链表，再比较。
        // 最后还要将后半部分链表恢复。
        // 反转部分可以参见 206 题的代码。
        return false;
    }
}

public class _234_PalindromeLinkedList {
    public static void main(String[] args) {
        System.out.println(5/2);
    }
}
