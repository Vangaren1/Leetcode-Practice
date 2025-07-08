package Grind75.week8.minimum_window_substring;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> retVal = new ArrayList<>();
        
        if ( nums.length == 0) return retVal;
        
        if ( nums.length == 1) { 
            retVal.add( Integer.toString(nums[0]));
            return retVal;
        }

        int ptr1 = 0;
        int ptr2 = 0;

        while ( ptr1 < nums.length) {

            while ( ptr2 < nums.length - 1) {
                int diff = Math.abs(nums[ptr2+1] - nums[ptr2]);
                if (diff == Integer.MIN_VALUE) break;
                if ( diff > 1){
                    break;
                }
                ptr2++;
            }
            
            retVal.add(strNum(nums[ptr1],nums[ptr2]));

            ptr1 = ptr2 + 1;
            ptr2++;

        }
        return retVal;

    }

    public String strNum(int a, int b) {
        if ( a == b) {
            return Integer.toString(a);
        }
        return Integer.toString(a) + "->" + Integer.toString(b);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] nums = {-2147483648,0,2,3,4,6,8,9};

        System.out.println(sol.summaryRanges(nums));
        System.out.println("Running minimum_window_substring...");
    }
}
