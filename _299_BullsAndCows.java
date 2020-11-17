package com.example.leetcode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution299 {
    public String getHint(String secret, String guess) {
    	// ·½·¨Ò»£ºArrayList
    	int bull = 0;
    	int cow = 0;
    	List<Character> arrayList1 = new ArrayList<Character>();
    	List<Character> arrayList2 = new ArrayList<Character>();
    	for (int i = 0; i < secret.length(); i++) {
    		if (secret.charAt(i) == guess.charAt(i)) {
    			bull++;
    		} else {
    			arrayList1.add(secret.charAt(i));
    			arrayList2.add(guess.charAt(i));
    		}
    	}
    	for (Character c : arrayList2) {
    		if (arrayList1.contains(c)) {
    			cow++;
    			arrayList1.remove(c);
    		}
    	}
    	System.out.println(arrayList1.toString() + arrayList2.toString());
    	return bull + "A" + cow + "B";
    }
}

public class _299_BullsAndCows {
	public static void main(String[] args) {
		Solution299 solution299 = new Solution299();
		System.out.println(solution299.getHint("1807", "7810"));
		System.out.println(solution299.getHint("1123", "0111"));
		System.out.println(solution299.getHint("1", "0"));
		System.out.println(solution299.getHint("1", "1"));
		System.out.println(solution299.getHint("111388336", "311196888"));
	}
}
