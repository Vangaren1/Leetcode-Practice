package Extra.reverse_vowels_345;

import java.util.HashSet;
import java.util.Set;

class Solution {
    public String reverseVowels(String s) {
        char[] a = s.toCharArray();

        int left = 0;
        int right = s.length() -1;

        Set<Character> vowels = new HashSet<>();
        
        for ( char c : "aeiouAEIOU".toCharArray()) {
            vowels.add(c);
        }

        boolean shifted = false;
        while ( left < right ) {
            while ( left < s.length() && !vowels.contains(a[left])){
                left++;
                shifted = true;
            }
            while ( right >= 0 && !vowels.contains(a[right])) {
                right--;
                shifted = true;
            }

            if (!shifted){
                char tmp = a[right];
                a[right] = a[left];
                a[left] = tmp;
                left++;
                right--;
            } else {
                shifted = false;
            }

        }

        return new String(a);
    }
    public static void main(String[] args) {
        Solution s = new Solution();

        String test = "IceCreAm";
        System.out.println(s.reverseVowels(test));
        System.out.println("Running reverse_vowels_345...");
    }
}
