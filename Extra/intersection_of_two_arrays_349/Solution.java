package Extra.intersection_of_two_arrays_349;

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {

        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();

        for (int tmp : nums1 ){
            set1.add(tmp);
        }

        for (int num : nums2 ){
            if (set1.contains(num)) set2.add(num);
        }

        int[] retArray = set2.stream().mapToInt(Integer::intValue).toArray();
        return retArray;
    }
    public static void main(String[] args) {
        System.out.println("Running intersection_of_two_arrays_349...");
    }
}
