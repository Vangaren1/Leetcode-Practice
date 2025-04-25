package Grind75.week2.longest_palindrome_409;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int longestPalindrome(String s) {
        int total = 0;

        Map<Character, Integer> count = new HashMap<>();

        for( char c : s.toCharArray()){
            count.put(c, count.getOrDefault(c, 0) + 1);
        }

        boolean foundOdd = false;
        for( int n : count.values()){
            total = total + n - (n % 2);
            if(n%2 == 1){
                foundOdd = true;
            }
        }
        if(foundOdd){
            total++;
        }

        return total;
    }
    public static void main(String[] args) {
        System.out.println("Running longest_palindrome_409...");
    }
}
