package Grind75.week5.combination_sum_39;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {

    List<List<Integer>> results = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<Integer> curr = new ArrayList<>();

        treefind(candidates, target, curr);
        
        return results;
    }

    public void treefind(int[] candidates, int target, List<Integer> current){
        int tmp=0;
        if(target == 0){
            Collections.sort(current);
            if(! results.contains(current)){
                results.add(current);
            }
        } else if(target > 0){    
            for(int n : candidates){
                tmp = target - n;
                if (tmp >=0){
                    List<Integer> newCurrent = new ArrayList<>(current);
                    newCurrent.add(n);
                    treefind(candidates, tmp, newCurrent);
                }
            }
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] candidates = new int[] {2,3,6,7};
        int target = 7;

        System.out.println(s.combinationSum(candidates, target));
        System.out.println("Running combination_sum_39...");
    }
}
