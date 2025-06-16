package Grind75.week6.subset_78;

import java.util.ArrayList;
import java.util.List;

class Solution {
    List<List<Integer>> results;

    List<Integer> current;
    int[] nums;

    public List<List<Integer>> subsets(int[] nums) {
        this.nums = nums;
        results = new ArrayList<>();
        current = new ArrayList<>();


        dfs(0);
        
        return results;

    }

    public void dfs(int index){

        if ( index >= nums.length){
            results.add(new ArrayList<>(current));
            return;
        }

        current.add(nums[index]);
        dfs(index+1);

        current.remove(current.size() -1);
        dfs(index+1);


    }
    public static void main(String[] args) {
        int[] nums = {1,2,3};

        Solution s = new Solution();

        System.out.println(s.subsets(nums));
        System.out.println("Running subset_78...");
    }
}
