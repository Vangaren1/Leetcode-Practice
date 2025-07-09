package Extra.range_sum_query_immutable_303;

class NumArray {
    int[] nums;
    int[] sums;
    public NumArray(int[] nums) {
        this.nums = nums;
        this.sums = new int[nums.length];
        
        this.sums[0] = nums[0];
        for ( int index = 1; index < this.nums.length; index ++  ) {
            this.sums[index] = this.nums[index] + this.sums[index-1];
        }

    }
    
    public int sumRange(int left, int right) {
        if ( left == 0) return sums[right];

        return sums[right] - sums[left- 1];
    }

    public static void main(String[] args) {

        int[] nums = {-2,0,3,-5,2,-1};
        NumArray n = new NumArray(nums);
        System.out.println(n.sumRange(0, 5));
        System.out.println("Running range_sum_query-immutable-303...");
    }
}
