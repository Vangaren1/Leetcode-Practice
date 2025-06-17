package Grind75.week6.longest_palindrome_5;

class Solution {

    String curr;

    public String longestPalindrome(String s) {
        if ( s == null || s.length() < 1){
            return "";
        }
        curr = new String(s);
        String longest = "";
        for ( int index = 0; index < s.length(); index++ ){
            String tmp = palinCheck(index);
            if ( tmp.length() > longest.length()){
                longest = tmp;
            }
        }
        
        return longest;
    }

    public String palinCheck(int index) {
        int ptr1 = index;
        int ptr2 = index; 
        int ptr3 = index;
        int ptr4 = index + 1;

        boolean even = ptr4 < curr.length() && curr.charAt(ptr3) == curr.charAt(ptr4);
        boolean odd = true;

        String currEven = "", currOdd = "";

        if (even) {
            currEven = curr.substring(ptr3, ptr4 + 1);
        } else {
            currOdd = curr.substring(ptr2, ptr1 + 1);
        }

        while (even || odd) {
            if (odd){
                if ( ptr2 < 0 || ptr1 == curr.length()){
                    break;
                }
                odd = curr.charAt(ptr2) == curr.charAt(ptr1);
                if (!odd){
                    continue;
                }
                currOdd = curr.substring(ptr2, ptr1 + 1);
                ptr2--;
                ptr1++;
            }

            if (even){
                if ( ptr3 < 0 || ptr4 == curr.length()){
                    break;
                }
                even = curr.charAt(ptr3) == curr.charAt(ptr4);
                if (!even){
                    continue;
                }
                currEven = curr.substring(ptr3, ptr4 + 1);
                ptr3--;
                ptr4++;
            }
        }
        if ( currEven.length() > currOdd.length() ){
            return currEven;
        }
        return currOdd;

    }
    public static void main(String[] args) {
        System.out.println("Running longest_palindrome_5...");
    }
}
