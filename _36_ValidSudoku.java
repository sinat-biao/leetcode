package com.example.leetcode;

import java.util.HashSet;

class Solution36 {
    public boolean isValidSudoku(char[][] board) {
        // 方法一：hash + 暴力检查
        // 1.先检查行
        for (int i = 0; i < board.length; i++) {
        	HashSet<Character> hashSet_row = new HashSet<Character>();
        	for (int j = 0; j < board[0].length; j++) {
        		if (board[i][j] == '.') {
        			continue;
        		}
        		if (hashSet_row.contains(board[i][j])) {
        			System.out.println("行冲突" + board[i][j]);
        			return false;
        		} else {
        			hashSet_row.add(board[i][j]);
        		}
        	}
        	hashSet_row.clear();
        }
        // 2.检查列
        for (int j = 0; j < board[0].length; j++) {
        	HashSet<Character> hashSet_col = new HashSet<Character>();
        	for (int i = 0; i < board.length; i++) {
        		if (board[i][j] == '.') {
        			continue;
        		}
        		if (hashSet_col.contains(board[i][j])) {
        			System.out.println("列冲突" + board[i][j]);
        			return false;
        		} else {
        			hashSet_col.add(board[i][j]);
        		}
        	}
        }
        // 3.检查九宫格
    	for (int i = 0; i < 9; i=i+3) {
    		for (int j = 0; j < 9; j=j+3) {
    			if (!nineisvalid(board, i, j, i+2, j+2)) {
    				return false;
    			}
    		}
    	}
        return true;
    }
    
    private boolean nineisvalid(char[][] board, int i_min, int j_min, int i_max, int j_max) {
    	HashSet<Character> hashSet = new HashSet<Character>();
		for (int i = i_min; i <= i_max; i++) {
			for (int j = j_min; j <= j_max; j++) {
				if (board[i][j] == '.') {
        			continue;
        		}
				if (hashSet.contains(board[i][j])) {
					return false;
				} else {
					hashSet.add(board[i][j]);
				}
			}
		}
    	return true;
	}
}

public class _36_ValidSudoku {
	public static void main(String[] args) {
		Solution36 solution36 = new Solution36();
		char[][] board = { 
						 {'5','3','.','.','7','.','.','.','.'}
						,{'6','.','.','1','9','5','.','.','.'}
						,{'.','9','8','.','.','.','.','6','.'}
						,{'8','.','.','.','6','.','.','.','3'}
						,{'4','.','.','8','.','3','.','.','1'}
						,{'7','.','.','.','2','.','.','.','6'}
						,{'.','6','.','.','.','.','2','8','.'}
						,{'.','.','.','4','1','9','.','.','5'}
						,{'.','.','.','.','8','.','.','7','9'}};
		System.out.println(solution36.isValidSudoku(board));
		System.out.println(solution36.isValidSudoku(new char[][] {{'8','3','.','.','7','.','.','.','.'}
				,{'6','.','.','1','9','5','.','.','.'}
				,{'.','9','8','.','.','.','.','6','.'}
				,{'8','.','.','.','6','.','.','.','3'}
				,{'4','.','.','8','.','3','.','.','1'}
				,{'7','.','.','.','2','.','.','.','6'}
				,{'.','6','.','.','.','.','2','8','.'}
				,{'.','.','.','4','1','9','.','.','5'}
				,{'.','.','.','.','8','.','.','7','9'}}));

	}
}
