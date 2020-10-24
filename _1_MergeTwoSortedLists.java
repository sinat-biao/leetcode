package com.leetcode.java;

/**
 * Merge two sorted linked lists and return it as a new sorted list.
 * The new list should be made by splicing together the nodes of the first two lists.
 */

class ListNode1 {
    int val;
    ListNode1 next;
    ListNode1() {}
    ListNode1(int val) { this.val = val; }
    ListNode1(int val, ListNode1 next) { this.val = val; this.next = next; }
}

class Solution1 {
    public ListNode1 mergeTwoLists(ListNode1 l1, ListNode1 l2) {
        if (l1 == null && l2 == null) {
            return null;
        }

        ListNode1 l3 = new ListNode1();
        ListNode1 start = l3;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                l3.val = l1.val;
                l3.next = new ListNode1();
                l3 = l3.next;
                l1 = l1.next;
            } else {
                l3.val = l2.val;
                l3.next = new ListNode1();
                l3 = l3.next;
                l2 = l2.next;
            }
        }
        if (l1 != null) {
            l3.val = l1.val;
            l3.next = l1.next;
        } else if (l2 != null){
            l3.val = l2.val;
            l3.next = l2.next;
        }
        return start;
    }
}

public class _1_MergeTwoSortedLists {
    public static void main(String[] args) {
        _1_MergeTwoSortedLists m = new _1_MergeTwoSortedLists();
        m.test1();
        System.out.println();
        m.test2();
    }

    public void test1() {
        Solution1 solution = new Solution1();
        ListNode1 l1 = new ListNode1(1);
        ListNode1 l2 = new ListNode1(1);
        ListNode1 l11 = new ListNode1(2);
        ListNode1 l12 = new ListNode1(4);
        ListNode1 l21 = new ListNode1(3);
        ListNode1 l22 = new ListNode1(4);
        l1.next = l11;
        l11.next = l12;
        l2.next = l21;
        l21.next = l22;
        ListNode1 l = solution.mergeTwoLists(l1, l2);
        while (l != null) {
            System.out.print(l.val + "-");
            l = l.next;
        }
    }

    public void test2() {
        Solution1 solution = new Solution1();
        ListNode1 l1 = null;
        ListNode1 l2 = null;
        ListNode1 l = solution.mergeTwoLists(l1, l2);
        while (l != null) {
            System.out.print(l.val + "-");
            l = l.next;
        }
    }
}
