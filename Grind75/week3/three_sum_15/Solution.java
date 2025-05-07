package Grind75.week3.three_sum_15;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> returnList = new ArrayList<>();
        Set<List<Integer>> seen = new HashSet<>();
        
        Arrays.sort(nums);

        int second, third;
        int fnum, snum, tnum, currSum;
        for(int first=0; first < nums.length - 1; first++){
            second = first + 1;
            third = nums.length -1;
            while( second < third){
                fnum = nums[first];
                snum = nums[second];
                tnum = nums[third]; 
                currSum = fnum + snum + tnum;
                if(currSum < 0){
                    second++;
                }else if(currSum > 0){
                    third--;
                }else{
                    List<Integer> tmp = Arrays.asList(fnum, snum, tnum);
                    if(!seen.contains(tmp)){
                        seen.add(tmp);
                        returnList.add(tmp);
                    }else{
                        second++;
                    }
                }
            }

        }

        return returnList;
    }
    public static void main(String[] args) {
        System.out.println("Running three_sum_15...");
    }
}
