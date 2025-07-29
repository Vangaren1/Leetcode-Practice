package Extra.find_all_numbers_disappeared_from_array_448;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> retList = new ArrayList<>();

        Set<Integer> inRange = new HashSet<>();

        for (int i = 0; i <= nums.length; i++) {
            inRange.add(i);
        }

        for (int n : nums) {
            if (inRange.contains(n)) {
                inRange.remove(n);
            }
        }

        return new ArrayList<>(inRange);
    }

    public static void main(String[] args) {
        System.out.println("Running find_all_numbers_disappeared_from_array_448...");
    }
}
