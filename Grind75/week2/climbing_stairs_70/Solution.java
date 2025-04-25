package Grind75.week2.climbing_stairs_70;

import java.util.HashMap;
import java.util.Map;

class Solution {

    Map<Integer, Integer> steps = new HashMap<>();
    

    public int climbStairs(int n) {
        this.steps.put(1,1);
        this.steps.put(2,2);
        return climbRec(n);
    }

    public int climbRec(int n){
        if(this.steps.containsKey(n)){
            return this.steps.get(n);
        }
        int tmp = climbRec(n-1) + climbRec(n-2);
        this.steps.put(n, tmp);
        return tmp;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(s.climbStairs(1));
        System.out.println(s.climbStairs(2));
        System.out.println(s.climbStairs(3));
        System.out.println(s.climbStairs(5));
        System.out.println("Running climbing_stairs_70...");
    }
}
