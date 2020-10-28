package com.leetcode.java;

import java.util.ArrayList;
import java.util.HashMap;

// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}

class Solution138 {
    public Node copyRandomList(Node head) {
        // 方法一：多次遍历
        Node l = head;
        int len = 0;
        // 首先获得现有节点的指向信息
        ArrayList<Node> arrayList = new ArrayList<>();
        HashMap<Node, Integer> hashMap = new HashMap<>();
        while (l != null) {
            hashMap.put(l, len);
            arrayList.add(l);
            len++;
            l = l.next;
        }
        // 获得 random 指向列表
        ArrayList<Integer> random = new ArrayList<>();
        for (int i = 0; i < len; i++) {
            if (arrayList.get(i).random == null) {
                random.add(null);
            } else {
                random.add(hashMap.get(arrayList.get(i).random));
            }
        }
        // 深拷贝
        Node pre = new Node(-1);
        Node start = pre;
        ArrayList<Node> arrayList1 = new ArrayList<>();
        for (Node node : arrayList) {
            pre.next = new Node(node.val);
            pre = pre.next;
            arrayList1.add(pre);
        }
        for (int i = 0; i < len; i++) {
            if (random.get(i) == null) {
                arrayList1.get(i).random = null;
            } else {
                arrayList1.get(i).random = arrayList1.get(random.get(i));
            }
        }
        return start.next;
    }

    public Node copyRandomList2(Node head) {
        // 方法二：二次遍历优化
        Node pre = new Node(-1);
        Node start = pre;
        int k = 0;
        HashMap<Node, Integer> hashMap = new HashMap<>();
        ArrayList<Node> arrayList = new ArrayList<>();
        while (head != null) {
            pre.next = new Node(head.val);
            pre = pre.next;
            pre.random = head.random;
            arrayList.add(pre);
            hashMap.put(head, k++);
            head = head.next;
        }
        pre.next = null;
        pre = start;
        while (pre != null) {
            if (pre.random != null) {
                pre.random = arrayList.get(hashMap.get(pre.random));
            }
            pre = pre.next;
        }
        return start.next;
    }
}

public class _138_CopyListWithRandomPointer {
}
