package com.leetcode.java;

/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

// 以下函数纯属凑数
class GuessGame {
    public int guess(int n) {
        return 1;
    }
}

class Solution374 extends GuessGame {
    public int guessNumber(int n) {
        int first = 1;
        int last = n;
        int mid;
        while (first <= last) {
            mid = first + (last - first) / 2;
            int gus;
            gus = guess(mid);
            if (gus == 0) {
                return mid;
            } else {
                if (gus == -1) {
                    last = mid - 1;
                } else {
                    first = mid + 1;
                }
            }
        }
        return -1;
    }
}

public class _374_GuessNumberHigherOrLower {
}
