package com.example.leetcode;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Stack;


class NestedIterator implements Iterator<Integer> {

    private List<NestedInteger> list2;
    private Stack<Integer> stack;

    public NestedIterator(List<NestedInteger> nestedList) {
        list2 = new ArrayList<NestedInteger>();
        stack = new Stack<Integer>();
        int i = 0;
        boolean iscyl = true;
        while (iscyl) {
        	while (i < nestedList.size()) {
        		if (nestedList.get(i).isInteger()) {
        			list2.add(nestedList.get(i));
        			i++;
        		} else {
        			for (NestedInteger ne : nestedList.get(i).getList()) {
        				list2.add(ne);
        			}
        			i++;
        		}
        	}   
        	iscyl = false;
        	for (NestedInteger nes : list2) {
        		if (!nes.isInteger()) {
        			iscyl = true;
        		}
        	}
        	i = 0;
        	if (iscyl) {
        		nestedList.clear();
        		for (NestedInteger nes : list2) {
        			nestedList.add(nes);
        		}
        		list2.clear();
        	}
        }
        for (NestedInteger nes : list2) {
        	System.out.print(nes.getInteger() + " ");
        }
        for (int i1 = list2.size() - 1; i1 >=0; i1--) {
        	stack.add(list2.get(i1).getInteger());
        }
    }

    @Override
    public Integer next() {
        return stack.pop();
    }

    @Override
    public boolean hasNext() {
        return !stack.isEmpty();
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */

public class _341_FlattenNestedListIterator {

}
