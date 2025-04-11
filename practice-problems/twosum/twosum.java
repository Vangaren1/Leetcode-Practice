import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> indexDict = new HashMap<>();

        for(int i = 0; i<nums.length; i++){
            indexDict.put(nums[i], i);
        }

        for(int j = 0; j< nums.length; j++ ){
            int curr = nums[j];
            int needed = target - curr;
            if( indexDict.containsKey(needed) && indexDict.get(needed) != j){
                return new int[] {j, indexDict.get(needed)};
            }
        }
        return new int[] {-1,-1};
    }
}