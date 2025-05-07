package Grind75.week3.longest_substring_without_repeating_characters_3;

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maximum = 0;
        int start = 0;

        Set<Character> seen = new HashSet<>();

        for( int index = 0; index < s.length(); index ++){
            char curr = s.charAt(index);
            while( seen.contains(curr)){
                seen.remove(s.charAt(start));
                start++;
            }
            seen.add(curr);
            maximum = Math.max(maximum, index - start + 1);
        }

        return maximum;
    }
    public static void main(String[] args) {
        System.out.println("Running longest_substring_without_repeating_characters_3...");
    }
}
