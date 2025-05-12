package Grind75.week4.product_of_array_except_self_238;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];
        int[] result = new int[nums.length];

        int tmp = 1;

        for ( int m = 0; m < nums.length; m++){
            prefix[m] = 1;
            suffix[m] = 1;
        }


        for ( int i = 1; i < nums.length; i++){
            prefix[i] = prefix[i-1] * nums[i-1];
        }
        for ( int j = nums.length-2; j > -1; j--){
            suffix[j] = suffix[j + 1] * nums[j+1];
        }

        for ( int k = 0; k < nums.length; k++) {
            result[k] = suffix[k] * prefix[k];
        }

        return result;   
    }
    public static void main(String[] args) {
        int[] nums = new int[] {1,2,3,4};
        Solution s = new Solution();

        System.out.println(s.productExceptSelf(nums));

        System.out.println("Running product_of_array_except_self_238...");
    }
}
