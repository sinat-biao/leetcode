package com.example.leetcode;

import java.util.HashMap;

class Solution166 {
    public String fractionToDecimal(int numerator, int denominator) {
    	// 方法一：模拟除法，并用栈判定是否重复
    	if (numerator == 0) {
            return "0";
        }
    	long numeratorlong = (long)numerator;
    	long denominatorlong = (long)denominator;
    	boolean needaddfuhao = false;
    	if ((numeratorlong < 0 && denominatorlong > 0) || (numeratorlong > 0 && denominatorlong < 0)) {
    		needaddfuhao = true;
    	}
    	numeratorlong = Math.abs(numeratorlong);
		denominatorlong = Math.abs(denominatorlong);
    	HashMap<Long, Integer> hashMap = new HashMap<Long, Integer>();
    	String re = "";
    	while (true) {
    		if (numeratorlong < denominatorlong) {
    			if (re == "" ) {
    				re += "0.";
    			} else {
    				if (!re.contains(".")) {
    					re += ".";
    				}
    			}
    			numeratorlong *= 10;
    			if (hashMap.containsKey(numeratorlong)) {
    				if (needaddfuhao) {
						return "-" + re.substring(0, hashMap.get(numeratorlong)) + "(" + re.substring(hashMap.get(numeratorlong)) + ")";
    				}
    				return re.substring(0, hashMap.get(numeratorlong)) + "(" + re.substring(hashMap.get(numeratorlong)) + ")";
    			}
    			hashMap.put(numeratorlong, re.length());
    			System.out.println(re);
    			while (numeratorlong < denominatorlong) {
    				numeratorlong *= 10;
					re += "0";
					if (hashMap.containsKey(numeratorlong)) {
						if (needaddfuhao) {
							return "-" + re.substring(0, hashMap.get(numeratorlong)) + "(" + re.substring(hashMap.get(numeratorlong)) + ")";
	    				} else {
	    					return re.substring(0, hashMap.get(numeratorlong)) + "(" + re.substring(hashMap.get(numeratorlong)) + ")";	    					
	    				}
					}
					hashMap.put(numeratorlong, re.length());
					System.out.println(re);
				}
    			
    		}
    		Long integer_sub = (long)(numeratorlong / denominatorlong);
    		numeratorlong = numeratorlong % denominatorlong;
    		if (numeratorlong == 0) {
    			re += integer_sub;
    			if (needaddfuhao) {
					return "-" + re;
				}
    			return re;
    		}
    		re += integer_sub;
//    		System.out.println(re);
    	}
    }
}

public class _166_FractionToRecurringDecimal {
	public static void main(String[] args) {
		Solution166 solution166 = new Solution166();
//		System.out.println(solution166.fractionToDecimal(1, 2));
//		System.out.println(solution166.fractionToDecimal(2, 1));
//		System.out.println(solution166.fractionToDecimal(2, 3));
////		System.out.println("0.5".split("\\.")[1]);
//		System.out.println(solution166.fractionToDecimal(4, 333));
//		System.out.println(solution166.fractionToDecimal(1, 5));
//		System.out.println(solution166.fractionToDecimal(56, 11));
//		System.out.println(solution166.fractionToDecimal(1, 6));
//		System.out.println(solution166.fractionToDecimal(1, 333));
//		System.out.println(solution166.fractionToDecimal(1, 17));
//		System.out.println(solution166.fractionToDecimal(-50, 8));
		System.out.println(solution166.fractionToDecimal(7, -12));
		System.out.println(solution166.fractionToDecimal(-2147483648, 1));
	}
}
