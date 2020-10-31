package com.leetcode.java;
/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

// 下面的函数是为了防止报错而写得，当不得真。
class VersionControl {
    public boolean isBadVersion(int n) {
        return true;
    }
}

class Solution278 extends VersionControl {
    public int firstBadVersion(int n) {
        // 二分搜索
        int first = 1;
        int last = n;
        int mid;
        int ans = 1;
        while (first <= last) {
            // mid = (first + last) / 2;
            mid = first + (last - first) / 2;
            if (isBadVersion(mid)){
                last = mid - 1;
                ans = mid;
            } else {
                first = mid + 1;
            }
        }
        return ans;
    }
}

public class _278_FirstBadVersion {
}
