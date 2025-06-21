package Grind75.week7.letter_combinations_of_a_phone_number_17;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<String> letterCombinations(String digits) {

        Map<Character, String> letters = new HashMap<>();
        letters.put('2', "abc");
        letters.put('3',"def");
        letters.put('4',"ghi");
        letters.put('5',"jkl");
        letters.put('6',"mno");
        letters.put('7',"pqrs");
        letters.put('8',"tuv");
        letters.put('9',"wxyz");

        List<String> results = new ArrayList<>();
        
        for (int index = 0; index < digits.length(); index++) {
            char currDigit = digits.charAt(index);
            String lett = letters.get(currDigit);
            List<String> tmpResults = new ArrayList<>();
            if ( results.size() == 0){
                for ( char tmp : lett.toCharArray() ) {
                    tmpResults.add(String.valueOf(tmp));
                }
            }else {
                for ( String tmp : results ) {
                    for ( char l : lett.toCharArray()){
                        tmpResults.add( tmp + l);
                    }
                }
            }
            results = tmpResults;

        }

        return results;
    }
    public static void main(String[] args) {
        System.out.println("Running letter_combinations_of_a_phone_number_17...");
    }
}
