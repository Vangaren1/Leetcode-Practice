package Extra.move_zeroes_283;

class Solution {
    boolean seenNonZero;
    public void moveZeroes(int[] nums) {
        seenNonZero = true;
        int ptr = 0;
        while (ptr < nums.length) {
            if( nums[ptr] == 0 && seenNonZero) {
                moveLeft(nums, ptr);
            }else{
                ptr++;
            }

        }    
    }

    public void moveLeft(int[] nums, int pos) {
        seenNonZero = false;
        for ( int index = pos; index < nums.length -1; index ++ ){
            if ( nums[index+1] != 0) seenNonZero=true;
            nums[index] = nums[index+1];
        }
        nums[nums.length-1] = 0;
    }

    public static void main(String[] args) {
        int[] nums = {0,0,0,0,0,0,1,1,1};
        Solution sol = new Solution();
        sol.moveZeroes(nums);
        System.out.println(nums);
        System.out.println("Running move_zeroes_283...");
    }
}
