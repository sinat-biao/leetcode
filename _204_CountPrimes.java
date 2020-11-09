package com.leetcode.java;

import java.util.ArrayList;

class Solution204 {
    private boolean isprime(int num) {
        // 判断 num 是否为素数
        if (num % 2 == 0 || num % 3 == 0 || num % 5 == 0 || num % 7 == 0) {
            return false;
        }
        for (int j = 2; j < (int)Math.sqrt(num) + 1; j++) {
            if (num % j == 0) {
                return false;
            }
        }
        return true;
    }

    public int countPrimes(int n) {
        // 方法一：遍历判断素数(超时)
        int count = 0;
        int sqt = (int)Math.sqrt(n);
        System.out.println(sqt);
        for (int i = 2; i < n; i++) {
            // 判断是否为素数
            boolean isprime = true;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    isprime = false;
                }
            }
            if (isprime) {
                count++;
            }
        }
        return count;
    }

    public int countPrimes2(int n) {
        // 方法二：方法一改进
        int count = 0;
        if (n <= 10) {
            for (int i = 2; i < n; i++) {
                if (isprime(i)) {
                    count++;
                }
            }
            return count;
        } else {
            count = 4;
            int i = 10;
            while (i < n) {
                i += 1;
                if (isprime(i)) {
                    count++;
                }
                i += 2;
                if (isprime(i)) {
                    count++;
                }
                i += 4;
                if (isprime(i)) {
                    count++;
                }
                i += 2;
                if (isprime(i)) {
                    count++;
                }
                i += 1;
            }
        }
        return count;
    }

    public int countPrimes3(int n) {
        // 方法三：素数筛法
        if(n<=1){
            return 0;
        }
        byte[] origin = new byte[n+1];
        int count = 0;
        for(int i=2;i<n;i++){
            if(origin[i] == 0){
                count++;
                int k = 2;
                while(i*k<=n){
                    origin[i*k] = 1;
                    k++;
                }
            }else{
                continue;
            }
        }
        return count;
    }
}

public class _204_CountPrimes {
    public static void main(String[] args) {
        Solution204 solution204 = new Solution204();
        System.out.println(solution204.countPrimes(10));
        System.out.println(solution204.countPrimes(0));
        System.out.println(solution204.countPrimes(1));
    }
}
