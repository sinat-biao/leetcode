package com.example.leetcode;

import java.util.ArrayList;
import java.util.List;

class MinStack {
	
	private ArrayList<Integer> arrayList;
	private int min_num = Integer.MAX_VALUE;
	
    /** initialize your data structure here. */
    public MinStack() {
        arrayList = new ArrayList<Integer>();
    }
    
    public void push(int x) {
    	arrayList.add(x);
    	if (x < min_num) {
    		min_num = x;
    	}
    }
    
    public void pop() {
    	arrayList.remove(arrayList.size()-1);
    	min_num = Integer.MAX_VALUE;
    	for (int k = 0; k < arrayList.size(); k++) {
    		if (min_num < arrayList.get(k)) {
    			min_num = arrayList.get(k);
    		}
    	}
    }
    
    public int top() {
    	return arrayList.get(arrayList.size()-1);
    }
    
    public int getMin() {
    	return min_num;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */

public class _155_MinStack {

}
