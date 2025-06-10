package Grind75.week6.partition_equal_subset_sum_416;

import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean canPartition(int[] nums) {
     
        int total = 0;
        for ( int n : nums){
            total = total + n;
        }

        if ( total % 2 == 1){
            return false;
        }

        int goal = total / 2;

        Set<Integer> numset = new HashSet<>();
        numset.add(0);

        for (int index=nums.length - 1; index > -1; index--){
            Set<Integer> newSet = new HashSet<>(numset);
            for (int s : newSet){
                numset.add( s + nums[index]);
            }
            if ( numset.contains(goal)){
                return true;
            }
        }
        return false;
    }
    public static void main(String[] args) {
        System.out.println("Running partition_equal_subset_sum_416...");
    }
}
