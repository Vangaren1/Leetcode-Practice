package Grind75.week5.permutations_46;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> permute(int[] nums) {

        List<List<Integer>> results = new ArrayList<>();

        for(int index = 0; index < nums.length; index++){
            int[] copyNums = copyIntArray(nums, index);
            int curr = nums[index];

            if ( copyNums.length == 0){
                List<List<Integer>> listOfLists = new ArrayList<>();
                List<Integer> base = new ArrayList<>();
                base.add(curr);
                listOfLists.add(base);
                return listOfLists;
            }
                
            List<List<Integer>> subList = permute(copyNums);

            for ( List<Integer> inner : subList){
                inner.add(0, curr);
                results.add(inner);
            }

        }

        return results;
    }

    public int[] copyIntArray(int[] original, int excludeIndex){
        int[] result = new int[original.length -1 ];

        int j = 0;
        for ( int i = 0; i < original.length; i++){
            if ( i == excludeIndex)
                continue;
            result[j++] = original[i];
        }

        return result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {1,2,3};
        System.out.println(s.permute(nums));
        System.out.println("Running permutations_46...");
    }
}
