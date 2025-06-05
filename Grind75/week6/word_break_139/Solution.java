package Grind75.week6.word_break_139;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[s.length()] = true;

        for ( int index = s.length() -1; index > -1; index--){
            for(String word : wordDict){
                if ( index + word.length() <= s.length()){
                    String sCurr = s.substring(index, index + word.length());
                    if( word.compareTo(sCurr) == 0){
                        dp[index] = dp[index + word.length()];
                    }
                }
                if ( dp[index] == true){
                    break;
                }
            }
        }
        
        return dp[0];
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        String st = "leetcode";
        List<String> wordDict = new ArrayList<>();
        wordDict.add("leet");
        wordDict.add("code");
        System.out.println(s.wordBreak(st, wordDict));
        System.out.println("Running word_break_139...");
    }
}
