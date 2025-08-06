package Grind75.week8.minimum_window_substring;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

class Solution {
    public String minWindow(String s, String t) {
        return "";
    }

    public boolean validSub(Map<Character, Integer> a, Map<Character, Integer> b) {
        if (b.keySet().size() > a.keySet().size())
            return false;
        for (char key : b.keySet()) {
            if (b.get(key) > a.get(key))
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println("Running minimum_window_substring...");
    }
}
