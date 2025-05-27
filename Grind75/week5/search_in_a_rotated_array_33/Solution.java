package Grind75.week5.search_in_a_rotated_array_33;

class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1; 
        int mid = (left + right) / 2;

        while( left < right && nums[mid] != target){
            int lastLeft = left;
            int lastRight = right;
            int lastMid = mid;

            if( nums[left] > nums[mid]){
                if( nums[mid] < target && target <= nums[right]){
                    left = mid + 1;
                }else{
                    right = mid -1;
                }
            }else{
                if( nums[left] <= target && target < nums[mid] ){
                    right = mid - 1;
                }else{
                    left = mid + 1;
                }
            }

            mid = (left + right ) /2 ;

            if( left == lastLeft && right == lastRight && mid == lastMid){
                return -1;
            }
        }
        if(nums[mid] != target){
            return -1;
        }
        return mid; 
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {3,1};
        int target = 1;
        System.out.println(s.search(nums, target));

        System.out.println("Running search_in_a_rotated_array_33...");
    }
}
