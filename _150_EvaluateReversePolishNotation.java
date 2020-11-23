package com.example.leetcode;

import java.util.Stack;

class Solution150 {
    public int evalRPN(String[] tokens) {
    	// ·½·¨Ò»£ºÕ»
    	Stack<Integer> stack = new Stack<Integer>();
    	int i = 0;
    	while (i < tokens.length) {
    		if (tokens[i].equals("+") || tokens[i].equals("-") || tokens[i].equals("*") || tokens[i].equals("/")) {
    			int a = stack.pop();
    			int b = stack.pop();
    			if (tokens[i].equals("+")) {
    				stack.add((int)(a + b));    				
    			}
    			if (tokens[i].equals("-")) {
    				stack.add((int)(b - a));
    			}
    			if (tokens[i].equals("*")) {
    				stack.add((int)(a * b));
    			}
    			if (tokens[i].equals("/")) {
    				stack.add((int)(b / a));
    			}
    		} else {
    			stack.add(Integer.valueOf(tokens[i]));
    		}
    		i++;
    	}
    	return stack.pop();
    }
}

public class _150_EvaluateReversePolishNotation {
	public static void main(String[] args) {
		Solution150 solution150 = new Solution150();
		System.out.println(solution150.evalRPN(new String[] {"2", "1", "+", "3", "*"}));
		System.out.println(solution150.evalRPN(new String[] {"4", "13", "5", "/", "+"}));
		System.out.println(solution150.evalRPN(new String[] {"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}));
	}
}
