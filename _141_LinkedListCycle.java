package com.leetcode.java;

import java.util.HashSet;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution141 {
    public boolean hasCycle(ListNode head) {
        // 方法一：哈希计数
        // 用哈希表存储链表节点，遍历的时候查看是否重复出现即可。
        HashSet<ListNode> hashSet = new HashSet<>();
        while (head != null) {
            System.out.print(hashSet);
            System.out.print(" " + head.val + "\n");
            if (hashSet.contains(head)) {
                return true;
            } else {
                hashSet.add(head);
                head = head.next;
            }
        }
        return false;
    }

    public boolean hasCycle2(ListNode head) {
        // 方法二：双指针（快慢指针）
        // 两个指针 i、j，两者的移动速度不一样，一旦在遍历过程中慢指针追上快指针，
        // 则说明存在环路。
        // 其中 j 每次移动 2 步，i 每次移动 1 步。
        ListNode i = null;
        ListNode j = null;
        i = head;
        j = head;
        while (i != null && j != null) {
            j = j.next;
            if (j != null && j == i) {
                return true;
            }
            if (j == null) {
                return false;
            }
            j = j.next;
            if (j != null && j == i) {
                return true;
            }
            i = i.next;
        }
        return false;
    }
}

public class _141_LinkedListCycle {
    public static void main(String[] args) {
        int[] in = new int[] {3, 2, 0, 4};
        int pos = 1;
        _141_LinkedListCycle linkedListCycle = new _141_LinkedListCycle();
        ListNode head = linkedListCycle.test(in, pos);
        Solution141 solution141 = new Solution141();
        System.out.println(solution141.hasCycle2(head));

        in = new int[] {1, 2};
        pos = 0;
        System.out.println(solution141.hasCycle2(linkedListCycle.test(in, pos)));

        in = new int[] {1};
        pos = -1;
        System.out.println(solution141.hasCycle2(linkedListCycle.test(in, pos)));

        in = new int[] {1, 2, 3, 1, 2, 3, 1, 2, 3};
        pos = -1;
        System.out.println(solution141.hasCycle2(linkedListCycle.test(in, pos)));
//        ListNode start = head;
//        while (start != null) {
//            System.out.println(start.val);
//            start = start.next;
//        }
    }

    public ListNode test(int[] ints, int pos) {
        // 从数组 ints 中构造链表
        ListNode start = null;
        ListNode posl = null;
        ListNode head = null;
        for (int i = 0; i < ints.length; i++) {
            if (i == 0) {
                head = new ListNode(ints[i]);
                start = head;
                if (pos == i) {
                    posl = head;
                }
            }
            else {
                ListNode s = new ListNode(ints[i]);
                head.next = s;
                head = head.next;
                if (pos == i) {
                    posl = head;
                }
            }
        }
        head.next = posl;
        return start;
    }
}
