package Extra.isomorphic_strings_205;

import java.util.HashMap;
import java.util.Map;

class Solution {

    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int sCount = 0;
        int tCount = 0;
        Map<Character, Integer> sDict = new HashMap<>();
        Map<Character, Integer> tDict = new HashMap<>();

        

        for ( int index = 0; index < s.length(); index++) {
            char sChar = s.charAt(index);
            char tChar = t.charAt(index);

            if ( !sDict.containsKey(sChar)){
                sDict.put(sChar,sCount);
                sCount++ ;
            }
            if ( !tDict.containsKey(tChar)){
                tDict.put(tChar,tCount);
                tCount++ ;
            }

            if (sDict.get(sChar) != tDict.get(tChar)) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        System.out.println("Running isomorphic_strings_205...");
    }
}
