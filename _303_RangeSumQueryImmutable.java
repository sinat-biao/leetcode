package com.example.leetcode;

class NumArray {
//    private int[] arr;
//    private Map<Pair<Integer, Integer>, Integer> hashMap = new HashMap<>();

    private int[] sum;

    public NumArray(int[] nums) {
//        arr = nums;
    	
        // 缓存1
//        for (int i = 0; i < nums.length; i++) {
//            int sum = 0;
//            for (int j = i; j < nums.length; j++) {
//                sum += nums[j];
//                hashMap.put(new Pair<Integer, Integer>(i, j), sum);
//            }
//        }

        // 缓存2
        sum = new int[nums.length+1];
        for (int i = 1; i <= nums.length; i++) {
            sum[i] = sum[i-1] + nums[i-1];
        } 
    }
    
    public int sumRange(int i, int j) {
        // 方法一：暴力法
        // 每次累加
//        int sum = 0;
//        for (int k = i; k <= j; k++) {
//            sum += arr[k];
//        }
//        return sum;

        // 方法二：缓存(超时)
        // 两种缓存方式：
        // 1.（超内存）添加二维数组，行代表 i，列代表 j，每个位置的值即为 i-j 的累加值，该二维矩阵只有上半部分（i <= j），则状态转移方程为：
        // d[i][i] = nums[i]
        // d[i][j] = d[i][j-1] + nums[j] = d[i-1][j] - nums[i]
        // 2.直接使用 map（超时）
//        return hashMap.get(new Pair<Integer, Integer>(i, j));

        // 方法三：缓存2（累积和）
        // 见官方题解
        return sum[j+1] - sum[i];
        
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */

public class _303_RangeSumQueryImmutable {
	public static void main(String[] args) {
		NumArray numArray = new NumArray(new int[] {-2,0,3,-5,2,-1});
	}
}
