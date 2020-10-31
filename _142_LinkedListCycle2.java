package com.leetcode.java;
import java.util.HashSet;

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
class Solution142 {
    public ListNode detectCycle(ListNode head) {
        // 方法一：哈希表
        HashSet<ListNode> hashSet = new HashSet<>();
        while (head != null) {
            if (hashSet.contains(head)) {
                return head;
            } else {
                hashSet.add(head);
            }
            head = head.next;
        }
        return null;
    }

    public ListNode detectCycle2(ListNode head) {
        // 方法二：循环判断子链表是否为循环链表
        if (head == null) {
            return null;
        }
        ListNode pre = new ListNode(-1);
        pre.next = head;
        if (!isCycle(head)){
            return null;
        }
        while (head != null) {
            pre.next = null;
            if (!isCycle(head)){
                return pre;
            }
            pre.next = head;
            pre = head;
            head = head.next;
        }
        return null;
    }

    public ListNode detectCycle3(ListNode head) {
        // 方法三：快慢指针进阶版
        // 快慢指针在遍历时，存在与入环点距离之间的数学关系，详情请参见官方题解：
        // https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode-solution/
        ListNode pre = new ListNode(-1);
        pre.next = head;
        ListNode i = pre;
        ListNode j = pre.next;
        // 先定位双指针的相遇点(这里要注意的是 j 每走 2 步的相遇点)
        while (j != null) {
            i = i.next;
            j = j.next;
            if (j == null) {
                return null;
            }
            j = j.next;
            if (j == null) {
                return null;
            }
            if (j == i) {
                break;
            }
        }
        ListNode str = head;
        while (str != i) {
            i = i.next;
            str = str.next;
        }
        return str;
    }

    public boolean isCycle(ListNode head) {
        // 判断链表是否有环
        ListNode pre = new ListNode(-1);
        pre.next = head;
        ListNode i = pre;
        ListNode j = pre.next;
        while (j != null) {
            i = i.next;
            j = j.next;
            if (j == null) {
                break;
            }
            if (j == i) {
                return true;
            }
            j = j.next;
            if (j == null) {
                break;
            }
            if (j == i) {
                return true;
            }
        }
        return false;
    }
}

public class _142_LinkedListCycle2 {
}
