package Grind75.week2.majority_element_169;

import java.util.Arrays;

class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }   
    public static void main(String[] args) {
        System.out.println("Running majority_element_169...");
    }
}
