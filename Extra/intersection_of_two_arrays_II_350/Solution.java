package Extra.intersection_of_two_arrays_II_350;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer, Integer> c1 = new HashMap<>();
        Map<Integer, Integer> c2 = new HashMap<>();

        List<Integer> retVal = new ArrayList<>();

        for ( int n : nums1){
            c1.merge(n, 1, Integer::sum);
        }
        for ( int m : nums2){
            c2.merge(m, 1, Integer::sum);
        }

        for ( int tmp : c1.keySet()) {
            int count = Integer.min(c1.get(tmp), c2.getOrDefault(tmp, 0));
            for ( int c = count; c > 0; c--){
                retVal.add(tmp);
            }
        }

        return retVal.stream().mapToInt(Integer::intValue).toArray();

    }
    public static void main(String[] args) {
        System.out.println("Running intersection_of_two_arrays_II_350...");
    }
}
