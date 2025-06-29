package Extra.Roman_To_Integer_13;

import java.util.HashMap;
import java.util.Map;

class Solution {
    Map<String, Integer> rDict;
    Map<String, Integer> odd; 


    public int romanToInt(String s) {
        rDict = new HashMap<>();
        odd = new HashMap<>();
        rDict.put("I",1);
        rDict.put("V",5);
        rDict.put("X",10);
        rDict.put("L",50);
        rDict.put("C",100);
        rDict.put("D",500);
        rDict.put("M",1000);

        odd.put("IV", 4);
        odd.put("IX", 9);
        odd.put("XL", 40);
        odd.put("XC", 90);
        odd.put("CD", 400);
        odd.put("CM", 900);

        int total = 0;
        if (s.length() == 0){
            return 0;
        }

        int ptr = 0;

        while ( ptr < s.length() ){
            String curr = s.substring(ptr,ptr+1);
            String next = "";
            if ( ptr < s.length() - 1 ){
                next = s.substring(ptr + 1, ptr + 2);
            }
            if ( odd.containsKey(curr+next)) {
                total = total + odd.get(curr+next);
                ptr = ptr + 2;
            }else {
                total = total + rDict.get(curr);
                ptr++;
            }

        }
        return total;
    }
    public static void main(String[] args) {
        String s = "MCMXCIV";

        Solution sol = new Solution();

        System.out.println(sol.romanToInt(s));
        System.out.println("Running Roman_To_Integer_13...");
    }
}
