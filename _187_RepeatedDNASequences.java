package com.example.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution187 {
    public List<String> findRepeatedDnaSequences(String s) {
    	// 方法一：暴力搜索
    	if (s.length() < 10) {
    		return new ArrayList<String>();
    	}
    	HashSet<String> hashSet = new HashSet<String>();
    	List<String> re = new ArrayList<String>();
    	for (int i = 0, j = 10; j <= s.length(); i++, j++) {
    		if (hashSet.contains(s.subSequence(i, j))) {
    			if (!re.contains(s.subSequence(i, j))) {
    				re.add(s.substring(i, j));    				
    			}
    		} else {
    			hashSet.add(s.substring(i, j));
    		}
    	}
    	return re;
    }
    
    public List<String> findRepeatedDnaSequences2(String s) {
    	// 方法二：Rabin-Karp 方法
    	// 使用散列值代表每个切片，进而节省字符串匹配的耗时
    	if (s.length() < 10) {
    		return new ArrayList<String>();
    	}
    	HashMap<Character, Integer> acgtDict = new HashMap<Character, Integer>();
    	acgtDict.put('A', 0);
    	acgtDict.put('C', 1);
    	acgtDict.put('G', 2);
    	acgtDict.put('T', 3);
    	int L = 10;
    	Set<Integer> hashSet = new HashSet<Integer>();
    	Set<String> output = new HashSet<String>();
    	String sub0 = s.substring(0, 10);
    	// 计算 s0 的散列值
    	int h0 = 0;
    	for (int i = 0; i < sub0.length(); i++) {
    		h0 += acgtDict.get(sub0.charAt(i)) * Math.pow(4, L - 1 - i);
    	}
    	hashSet.add(h0);
    	System.out.println(h0);
    	for (int i = 1, j = 11; j <= s.length(); i++, j++) {
    		String subStr = s.substring(i, j);
    		int hNew = (int) ((h0 * 4 - acgtDict.get(s.charAt(i-1)) * Math.pow(4, L)) + acgtDict.get(s.charAt(j-1)));
    		h0 = hNew;
    		if (hashSet.contains(hNew)) {
    			output.add(subStr);
    		} else {
    			hashSet.add(hNew);
    		}
    	}
    	return new ArrayList<String>(output);
    }
}

public class _187_RepeatedDNASequences {
	public static void main(String[] args) {
		Solution187 solution187 = new Solution187();
		System.out.println(solution187.findRepeatedDnaSequences2("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"));
		System.out.println(solution187.findRepeatedDnaSequences2("AAAAAAAAAAAAA"));
		System.out.println(solution187.findRepeatedDnaSequences2("AAAAAAAAAAA"));
	}
}
