package com.leetcode.java;

//class ListNode {
//    int val;
//    ListNode next;
//    ListNode(int x) { val = x; }
//}

class Solution83 {
    public ListNode deleteDuplicates(ListNode head) {
    	ListNode start = head;
    	ListNode pre = head;
        head = head.next;
        while (head != null) {
            if (pre.val == head.val) {
                pre.next = head.next;
                head = head.next;
                continue;
            }
            pre = pre.next;
            head = head.next;
        }
        return start;
    }
}

public class _83_RemoveDuplicatesFromSortedList {
    public static void main(String[] args) {
        _83_RemoveDuplicatesFromSortedList m = new _83_RemoveDuplicatesFromSortedList();
        m.test1();
    }

    public void test1() {
        Solution83 solution = new Solution83();
        ListNode l = new ListNode(1);
        ListNode l1 = new ListNode(1);
        ListNode l2 = new ListNode(2);
        l.next = l1;
        l1.next = l2;
        ListNode r = solution.deleteDuplicates(l);
        while (r != null) {
            System.out.print(r.val + "-");
            r = r.next;
        }
    }
}
