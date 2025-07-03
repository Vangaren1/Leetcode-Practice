package Extra.happy_number_202;

import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();        
        while(true){
            if ( n == 1) return true;
            if ( seen.contains(n)) return false;
            seen.add(n);
            n = convert(n);
        }
    }

    public int convert(int n){
        String num = Integer.toString(n);
        int total = 0;
        for( char c: num.toCharArray()){
            int tmp = c - '0';
            tmp = tmp * tmp;
            total = total + tmp;
        }
        return total;
    }
    public static void main(String[] args) {
        System.out.println("Running happy_number_202...");
    }
}
