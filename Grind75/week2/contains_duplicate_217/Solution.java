package Grind75.week2.contains_duplicate_217;

import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> found = new HashSet<>();
        for(int n : nums){
            if(found.contains(n)){
                return true;
            }
            found.add(n);
        }
        return false;
    }
    public static void main(String[] args) {
        System.out.println("Running contains_duplicate_217...");
    }
}
