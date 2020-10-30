package com.leetcode.java;

import javax.swing.*;
import java.lang.reflect.Array;
import java.util.*;

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
class Solution148 {

    public void quicksort(ArrayList<ListNode> arrayList, int low, int high) {
        ListNode tmp;
        int i = low;
        int j = high;
        if (i < j){
            tmp = arrayList.get(low);
            while (i < j) {
                while (i < j && arrayList.get(j).val > tmp.val) {
                    j--;
                }
                if (i < j) {
                    arrayList.set(i, arrayList.get(j));
                    i++;
                }
                while (i < j && arrayList.get(i).val < tmp.val) {
                    i++;
                }
                if (i < j) {
                    arrayList.set(j, arrayList.get(i));
                    j--;
                }
            }
            arrayList.set(i, tmp);
            quicksort(arrayList, 0, i-1);
            quicksort(arrayList, i+1, high);
        }
    }

    public ListNode sortList(ListNode head) {
        // 方法一：快速排序+数组实现(超时)
        if (head == null) {
            return null;
        }
        ArrayList<ListNode> arrayList = new ArrayList<>();
        while (head != null) {
            arrayList.add(head);
            head = head.next;
        }
        int i = 0;
        int j = arrayList.size() - 1;
        quicksort(arrayList, i, j);
        ListNode pre = new ListNode(-1);
        head = pre;
        for (ListNode a : arrayList) {
            pre.next = a;
            pre = pre.next;
            System.out.print(a.val + " ");
        }
        pre.next = null;
        return head.next;
    }

    public ListNode sortList2(ListNode head) {
        // 方法二：方法一优化（超时）
        // 方法一中，第一次遍历只是为了构造 ArrayList，没有利用到排序信息
        if (head == null) {
            return null;
        }
        ListNode pre = new ListNode(-1);
        pre.next = head;
        LinkedList<ListNode> linkedList = new LinkedList<>();
        while (head != null) {
            if (linkedList.isEmpty()) {
                linkedList.add(head);
            } else {
                int i = 0;
                while (i < linkedList.size() && linkedList.get(i).val <= head.val) {
                    i++;
                }
                linkedList.add(i, head);
            }
            head = head.next;
        }
        head = pre;
        for (ListNode ln : linkedList) {
            pre.next = ln;
            pre = pre.next;
        }
        pre.next = null;
        return head.next;
    }

    public ListNode sortList3(ListNode head) {
        // 方法三：java 函数对 ArrayLis 排序
        ArrayList<ListNode> arrayList = new ArrayList<>();
        while (head != null) {
            arrayList.add(head);
            head = head.next;
        }
        Collections.sort(arrayList, new Comparator<ListNode>() {
            @Override
            public int compare(ListNode listNode, ListNode t1) {
                // 升序
                return listNode.val - t1.val;
            }
        });
        ListNode pre = new ListNode(-1);
        head = pre;
        for (ListNode l : arrayList) {
            pre.next = l;
            pre = pre.next;
        }
        pre.next = null;
        return head.next;
    }

    public ListNode sortList4(ListNode head) {
        // 方法四：归并排序
        if (head == null || head.next == null) {
            return head;
        }
        // 使用快慢节点搜寻中点，因为快指针每次走两步，慢指针每次走一步，所以快指针走过的路程正好是慢指针的 2 倍，
        // 当快指针走到末尾时，慢指针刚好在中点。
        ListNode fast = head.next;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode mid = slow.next;
        // 从中点处将链表断开
        slow.next = null;
        // 递归
        ListNode left = sortList4(head);
        ListNode right = sortList4(mid);
        // 归并
        ListNode pre = new ListNode(-1);
        ListNode prec = pre;
        while (left != null && right != null) {
            if (left.val <= right.val) {
                pre.next = left;
                left = left.next;
            } else {
                pre.next = right;
                right = right.next;
            }
            pre = pre.next;
        }
        if (left != null) {
            pre.next = left;
        }
        if (right != null) {
            pre.next = right;
        }
        return prec.next;
    }

    public void mergeSort(ListNode pre, ListNode first, ListNode last) {

    }

    public ListNode merge(ListNode list1, ListNode list2) {
        // 合并两个链表
        ListNode pre = new ListNode(-1);
        ListNode prec = pre;
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                pre.next = list1;
                list1 = list1.next;
            } else {
                pre.next = list2;
                list2 = list2.next;
            }
            pre = pre.next;
        }
        pre.next = null;
        return prec.next;
    }
}

public class _148_SortList {

    public void test() {
        int[] arr = new int[] {1,4, 6, 3, 2, 9, 7};
        System.out.println(Arrays.toString(arr));
        ListNode pre = new ListNode(-1);
        ListNode head = pre;
        for (int i = 0; i < arr.length; i++) {
            pre.next = new ListNode(arr[i]);
            pre = pre.next;
        }
        pre.next = null;
        pre = head;
        head = head.next;
        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
        System.out.println();
        head = pre.next;
        Solution148 solution148 = new Solution148();
        solution148.sortList4(head);
        while (head != null) {
            System.out.print(head.val + "-");
            head = head.next;
        }
    }

    public static void main(String[] args) {
//        int[] arr = new int[] {1,4, 6, 3, 2, 9, 7};
//        System.out.println(Arrays.toString(arr));
//        int[] temp = new int[arr.length];
        _148_SortList sortList = new _148_SortList();
//        sortList.mergeSort(arr, 0, arr.length-1, temp);
//        System.out.println(Arrays.toString(arr));
        sortList.test();
    }

    public void mergeSort(int[] arr, int first, int last, int[] temp) {
        if (first < last) {
            int mid = (first + last) / 2;
            mergeSort(arr, first, mid, temp);
            mergeSort(arr, mid + 1, last, temp);
            merge(arr, first, mid, last, temp);
        }

    }

    public void merge(int[] arr, int first, int mid, int last, int[] temp) {
        int i = first, j = mid + 1; // i为第一组的起点, j为第二组的起点
        int m = mid, n = last;  // m为第一组的终点, n为第二组的终点
        int k = 0;
        while (i <= m && j <= n) {  // 将两个有序序列循环比较, 填入数组temp
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
            }
        }
        while (i <= m) {
            temp[k++] = arr[i++];
        }
        while (j <= n) {
            temp[k++] = arr[j++];
        }
        for (i = 0; i < k; i++) {
            arr[first + i] = temp[i];
        }
    }
}
