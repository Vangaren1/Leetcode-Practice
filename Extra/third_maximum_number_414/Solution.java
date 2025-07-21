package Extra.third_maximum_number_414;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int thirdMax(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int n : nums) {
            seen.add(n);
        }

        int[] newNums = seen.stream().mapToInt(Integer::intValue).toArray();

        Arrays.sort(newNums);

        if (newNums.length < 3)
            return newNums[newNums.length - 1];

        return newNums[newNums.length - 3];
    }

    public static void main(String[] args) {
        System.out.println("Running third_maximum_number_414...");
    }
}
