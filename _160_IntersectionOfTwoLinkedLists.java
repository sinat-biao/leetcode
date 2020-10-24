package com.leetcode.java;

import java.util.ArrayList;
import java.util.List;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

class Solution160 {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // 方法一：列表记录法
        // 用两个列表分别存储两个链表的节点，然后从后往前遍历判断元素是否相同
        ArrayList<ListNode> listA = new ArrayList<>();
        ArrayList<ListNode> listB = new ArrayList<>();
        while (headA != null) {
            listA.add(headA);
            headA = headA.next;
        }
        while (headB != null) {
            listB.add(headB);
            headB = headB.next;
        }
        if (listA.isEmpty()) {
            return null;
        }
        if (listB.isEmpty()) {
            return null;
        }
        int i = listA.size() - 1, j = listB.size() - 1;
        for (; i >= 0 && j >= 0; i--, j--) {
            if (listA.get(i) != listB.get(j)) {
                if (i == listA.size() - 1) {
                    return null;
                } else {
                    return listA.get(i+1);
                }
            }
        }
        if (i > 0 || j > 0) {
            if (i < 0){
                return listA.get(i);
            } else {
                return listB.get(j);
            }
        } else {
            return listA.get(i);
        }
    }

    public ListNode getIntersectionNode2(ListNode headA, ListNode headB) {
        // 方法二：双指针法
        // 两个指针 pA 和 pB 分别指向 A 和 B 的头结点，并向后遍历，
        // 若 pA 到达末尾，则让其指向 B 的头结点，pB 到达末尾，则让其指向 A 的头结点。
        // 这样由于 pA 和 pB 各自走过自己和对方的路径，所以他们走的总的路径数是一致的，
        // 而交点之后的路径一致，所以 2 遍时 pA 和 pB 必然在交点处相遇。
        // 若 A 和 B 不相交，则 2 遍后双方都指向 null；
        if (headA == null || headB == null) {
            return null;
        }
        if (headB == headA) {
            return headA;
        }
        ListNode pA = headA;
        ListNode pB = headB;
        boolean isFirstA = true, isFirstB = true;
        while (true) {
            pA = pA.next;
            pB = pB.next;
            if (isFirstA && pA == null) {
                pA = headB;
                isFirstA = false;
            }
            if (isFirstB && pB == null) {
                pB = headA;
                isFirstB = false;
            }
            if (pA == pB) {
                return pA;
            }
        }
    }
}

public class _160_IntersectionOfTwoLinkedLists {
    public static void main(String[] args) {
        int intersectVal = 8;
        int[] listA = new int[] {4, 1, 8, 4, 5};
        int[] listB = new int[] {5, 0, 1, 8, 4, 5};
        int skipA = 2;
        int skipB = 3;
        _160_IntersectionOfTwoLinkedLists intersectionOfTwoLinkedLists = new _160_IntersectionOfTwoLinkedLists();
        ListNode[] list = intersectionOfTwoLinkedLists.test(intersectVal, listA, listB, skipA, skipB);
        ListNode headA = list[0];
        ListNode headB = list[1];
        Solution160 solution160 = new Solution160();
        System.out.println(solution160.getIntersectionNode2(headA, headB).val);
    }

    public ListNode[] test(int intersectVal, int[] listA, int[] listB, int skipA, int skipB) {
        ListNode headA = new ListNode(-1);
        ListNode headB = new ListNode(-1);
        ListNode sA = headA;
        ListNode sB = headB;
        int i = 0;
        int j = 0;
        for (; i < skipA; i++) {
            headA.next = new ListNode(listA[i]);
            headA = headA.next;
        }
        for (; j < skipB; j++) {
            headB.next = new ListNode(listB[j]);
            headB = headB.next;
        }
        for (; i < listA.length; i++) {
            headA.next = new ListNode(listA[i]);
            headB.next = headA.next;
            headA = headA.next;
            headB = headB.next;
        }
        ListNode[] list = new ListNode[] {sA.next, sB.next};
        return list;
    }
}
