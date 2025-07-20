package Extra.find_the_difference_389;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;


class Solution {
    public char findTheDifference(String s, String t) {
        Map<Character, Integer> sDict = new HashMap<>();
        Map<Character, Integer> tDict = new HashMap<>();

        for (char sh : s.toCharArray()) {
            sDict.merge(sh, 1, Integer::sum);
        }
        for (char th : t.toCharArray()) {
            tDict.merge(th, 1, Integer::sum);
        }
        
        for (char tmp : tDict.keySet() ){
            if ( sDict.getOrDefault(tmp, 0) != tDict.getOrDefault(tmp, 0)) return tmp;
        }

        return ' ';
    }
    public static void main(String[] args) {
        System.out.println("Running find_the_difference_389...");
    }
}
