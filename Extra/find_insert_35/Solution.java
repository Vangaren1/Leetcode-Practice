package Extra.find_insert_35;

class Solution {
    public int searchInsert(int[] nums, int target) {
        int find = search(nums, target);
        if ( nums[find] < target ){
            return find + 1;
        }
        return find;
    }

    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length -1;
        int mid = ( left + right ) / 2;

        while ( left < right ){
            int curr = nums[mid];
            if ( curr == target) {
                return mid;
            } else if (curr < target){
                left = mid + 1;
            } else {
                if ( mid == 0) return 0;
                right = mid - 1;
            }
            mid = (left + right ) / 2 ;

        }
        return mid;
    }
    public static void main(String[] args) {
        System.out.println("Running find_insert_35...");
    }
}
