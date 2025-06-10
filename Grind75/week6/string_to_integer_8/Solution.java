package Grind75.week6.string_to_integer_8;

import java.util.ArrayList;
import java.util.List;

class Solution {

    public int myAtoi(String s) {
        long total = 0;
        int ptr = 0;
        int len = s.length();
        while ( ptr < len && s.charAt(ptr) == ' '){
            ptr ++;
        }

        if ( ptr >= len){
            return 0;
        }

        int sign = 1;
        if ( s.charAt(ptr) == '-' || s.charAt(ptr) == '+'){
            if (s.charAt(ptr) == '-' ){
                sign = -1;
            }
            ptr++;
        }

        while ( ptr < len && s.charAt(ptr) == '0'){
            ptr ++;
        }


        while ( ptr < len && Character.isDigit( s.charAt(ptr))){
            int tmp = s.charAt(ptr) - '0';
            total = total * 10 + tmp;

            if (total > Integer.MAX_VALUE){
                break;
            }

            ptr++;
        }

        total = total * sign;


        if (sign == -1 && total < Integer.MIN_VALUE){
            return Integer.MIN_VALUE;
        }
        if (sign == 1 && total > Integer.MAX_VALUE){
            return Integer.MAX_VALUE;
        }
        
        
        return (int) total;
    }
    public static void main(String[] args) { 
        List<String> examples = new ArrayList<>();
        examples.add("-6147483648");
        examples.add("42");
        examples.add("   -042");
        examples.add("1337c0d3");
        examples.add("0-1");
        examples.add("words and 987");
        examples.add("    0000000000000   ");
        examples.add("21474836480");
        examples.add("-21474836480");
        Solution s = new Solution();
        for (String tmp : examples){
            System.out.println(s.myAtoi(tmp));
        }
        System.out.println("Running string_to_integer_8...");
    }
}
