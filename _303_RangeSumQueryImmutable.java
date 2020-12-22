package com.example.leetcode;

class NumArray {
//    private int[] arr;
//    private Map<Pair<Integer, Integer>, Integer> hashMap = new HashMap<>();

    private int[] sum;

    public NumArray(int[] nums) {
//        arr = nums;
    	
        // ����1
//        for (int i = 0; i < nums.length; i++) {
//            int sum = 0;
//            for (int j = i; j < nums.length; j++) {
//                sum += nums[j];
//                hashMap.put(new Pair<Integer, Integer>(i, j), sum);
//            }
//        }

        // ����2
        sum = new int[nums.length+1];
        for (int i = 1; i <= nums.length; i++) {
            sum[i] = sum[i-1] + nums[i-1];
        } 
    }
    
    public int sumRange(int i, int j) {
        // ����һ��������
        // ÿ���ۼ�
//        int sum = 0;
//        for (int k = i; k <= j; k++) {
//            sum += arr[k];
//        }
//        return sum;

        // ������������(��ʱ)
        // ���ֻ��淽ʽ��
        // 1.�����ڴ棩��Ӷ�ά���飬�д��� i���д��� j��ÿ��λ�õ�ֵ��Ϊ i-j ���ۼ�ֵ���ö�ά����ֻ���ϰ벿�֣�i <= j������״̬ת�Ʒ���Ϊ��
        // d[i][i] = nums[i]
        // d[i][j] = d[i][j-1] + nums[j] = d[i-1][j] - nums[i]
        // 2.ֱ��ʹ�� map����ʱ��
//        return hashMap.get(new Pair<Integer, Integer>(i, j));

        // ������������2���ۻ��ͣ�
        // ���ٷ����
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
