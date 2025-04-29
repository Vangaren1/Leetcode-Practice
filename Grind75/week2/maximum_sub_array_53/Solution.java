package Grind75.week2.maximum_sub_array_53;

class Solution {
    public int maxSubArray(int[] nums) {
        int maxsum = nums[0];
        int currSum = 0;
        for(int n: nums){
            if(currSum < 0){
                currSum = 0;
            }
            currSum += n;
            maxsum = Math.max(maxsum, currSum);
        }
        return maxsum;
    }
    public static void main(String[] args) {
        System.out.println("Running maximum_sub_array_53...");
    }
}
