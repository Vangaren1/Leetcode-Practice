package Grind75.week1.binary_search_704;

class Solution {
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length;
        int last = -1;
        int mid = (start + end) / 2;
        while(nums[mid] != target){
            if(nums[mid] > target){
                end = mid -1;
            }else{
                start = mid + 1;
            }
            last = mid;
            mid = (start + end ) / 2;
            if(mid >= nums.length || mid == last){
                return -1;
            }
        }
        return mid;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {-1,0,3,5,9,12};
        int target = 13;

        System.out.println(s.search(nums, target));

        System.out.println("Running binary_search_704...");
    }
}
