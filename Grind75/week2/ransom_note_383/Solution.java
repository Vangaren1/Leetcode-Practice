package Grind75.week2.ransom_note_383;

import java.util.HashMap;
import java.util.Map;

class Solution {

    public boolean canConstruct(String ransomNote, String magazine) {
        
        Map<Character, Integer> letters = new HashMap<>();
        int count = 0;
        for(char c : magazine.toCharArray()){
            count = letters.getOrDefault(c, 0) + 1;
            letters.put(c,  count);
        }
        for(char c: ransomNote.toCharArray()){
            count = letters.getOrDefault(c, 0) -1;
            if(count < 0){
                return false;
            }
            letters.put(c, count);
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println("Running ransom_note_383...");
    }
}
