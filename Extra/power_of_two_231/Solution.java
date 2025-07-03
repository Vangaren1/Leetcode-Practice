package Extra.power_of_two_231;

class Solution {
    public boolean isPowerOfTwo(int n) {
        if ( n < 1) return false;
        if ( n == 1) return true;
        if ( n % 2 == 1 ) return false;
        
        while ( (n & 2) != 2) {
            n = n >> 1;
        }
        return n == 2;
    }
    public static void main(String[] args) {
        System.out.println("Running power_of_two_231...");
    }
}
