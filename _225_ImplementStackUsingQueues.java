package com.example.leetcode;

import java.util.LinkedList;
import java.util.Queue;

class MyStack {

	private Queue<Integer> queue1;
	private Queue<Integer> queue2;
	
    /** Initialize your data structure here. */
    public MyStack() {
    	queue1 = new LinkedList<Integer>();
    	queue2 = new LinkedList<Integer>();
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
    	if (queue1.isEmpty()) {
    		queue2.offer(x);
    	} else {
    		queue1.offer(x);
    	}
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
    	if (!queue1.isEmpty()) {
    		while (!queue1.isEmpty()) {
    			Integer p1 = queue1.poll();
    			Integer p2 = queue1.poll();
    			if (p2 == null) {
    				return p1;
    			} else {
    				queue2.offer(p1);
    				if (queue1.element() == null) {
    					return p2;
    				} else {
    					queue2.offer(p2);
    				}
    			}
    		}
    	} else if (!queue2.isEmpty()) {
    		while (!queue2.isEmpty()) {
    			Integer p1 = queue2.poll();
    			Integer p2 = queue2.poll();
    			if (p2 == null) {
    				return p1;
    			} else {
    				queue1.offer(p1);
    				if (queue2.element() == null) {
    					return p2;
    				} else {
    					queue1.offer(p2);
    				}
    			}
    		}
    	} else {
    		return 0;
    	}
		return 0;
    }
    
    /** Get the top element. */
    public int top() {
    	if (queue1.isEmpty() && queue2.isEmpty()) {
    		return 0;
    	}
    	if (!queue1.isEmpty()) {
    		while (!queue1.isEmpty()) {
    			Integer p1 = queue1.poll();
    			Integer p2 = queue1.poll();
    			if (p2 == null) {
    				queue2.offer(p1);
    				return p1;
    			} else {
    				queue2.offer(p1);
    				queue2.offer(p2);
    				if (queue1.element() == null) {
    					return p2;
    				}
    			}
    		}
    	} 
    	if (!queue2.isEmpty()) {
    		while (!queue2.isEmpty()) {
    			Integer p1 = queue2.poll();
    			Integer p2 = queue2.poll();
    			if (p2 == null) {
    				queue1.offer(p1);
    				return p1;
    			} else {
    				queue1.offer(p1);
    				queue1.offer(p2);
    				if (queue2.element() == null) {
    					return p2;
    				}
    			}
    		}
    	} else {
    		return 0;
    	}
		return 0;
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
    	if (queue1.isEmpty() && queue2.isEmpty()) {
    		return true;
    	} else {
    		return false;
    	}
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */

public class _225_ImplementStackUsingQueues {

}
