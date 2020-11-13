package com.example.leetcode;

import java.util.ArrayList;

class Solution389 {
    public char findTheDifference(String s, String t) {
    	// ·½·¨Ò»£ºlist
    	ArrayList<Character> arrayList1 = new ArrayList<Character>();
    	for (int i = 0; i < s.length(); i++) {
    		arrayList1.add(s.charAt(i));
    	}
    	for (int i = 0; i < t.length(); i++) {
    		if (!arrayList1.contains(Character.valueOf(t.charAt(i)))) {
    			return t.charAt(i);
    		} else {
    			arrayList1.remove(Character.valueOf(t.charAt(i)));
    		}
    	}
    	return arrayList1.get(0);
    }
}

public class _389_FindTheDifference {
	public static void main(String[] args) {
		Solution389 solution389 = new Solution389();
		System.out.println(solution389.findTheDifference("abcd", "abcde"));
		System.out.println(solution389.findTheDifference("", "y"));
		System.out.println(solution389.findTheDifference("a", "aa"));
		System.out.println(solution389.findTheDifference("ae", "aea"));
	}
}
