package com.company;

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {1,2,3,4};
        int[] ans = sol.runningSum(nums);
        for(int i=0;i<ans.length;i++)
            System.out.print(ans[i]+" ");
        System.out.println("hello world");
    }
}


