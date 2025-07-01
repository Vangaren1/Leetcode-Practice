package Extra.single_number_136;

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int singleNumber(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for( int n : nums) {
            if (seen.contains(n)){
                seen.remove(n);
            } 
            else{
                seen.add(n);
            }
        }
        
        return seen.iterator().next();
    }
    public static void main(String[] args) {
        System.out.println("Running single_number_136...");
    }
}
