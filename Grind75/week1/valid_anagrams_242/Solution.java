package Grind75.week1.valid_anagrams_242;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> map1 = new HashMap<>();
        for(char c: s.toCharArray()){
            map1.put(c, map1.getOrDefault(c,0)+1);
        }

        Map<Character, Integer> map2 = new HashMap<>();
        for(char c: t.toCharArray()){
            map2.put(c, map2.getOrDefault(c,0)+1);
        }

        return map1.equals(map2);
        
    }

    public static void main(String[] args) {
        String s = "cat";
        String t = "rat";

        Solution sol = new Solution();

        boolean result = sol.isAnagram(s, t);

        System.out.println("Running valid_anagrams_242...");
    }
}
