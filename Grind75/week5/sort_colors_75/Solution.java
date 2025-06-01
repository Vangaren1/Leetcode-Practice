package Grind75.week5.sort_colors_75;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public void sortColors(int[] nums) {

        Map<Integer, Integer> colorCount = new HashMap<>();

        for ( int n : nums){
            if( !colorCount.containsKey(n)){
                colorCount.put(n, 1);
            }else{
                colorCount.put(n, colorCount.get(n) + 1);
            }
        }

        Set<Integer> keys = colorCount.keySet();
        List<Integer> keyList = new ArrayList<>(keys);
        Collections.sort(keyList);

        int curr = 0;

        for ( int index = 0; index < nums.length ; index ++ ){
            curr = keyList.get(0);
            nums[index] = curr;
            colorCount.put(curr, colorCount.get(curr) - 1);
            if ( colorCount.get(curr) == 0){
                keyList.remove(0);
            }
        }


        
        
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        int[] colors = {2,1,0,2,1,0};
        s.sortColors(colors);
        System.out.println(colors);
        System.out.println("Running sort_colors_75...");
    }
}
