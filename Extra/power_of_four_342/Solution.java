package Extra.power_of_four_342;

class Solution {
    public boolean isPowerOfFour(int n) {
        if ( n <= 0) return false;
        if ( n == 1) return true;
        if ( n < 4 && (n%4)!= 0) return false;
        return isPowerOfFour(n >> 2);    
    }
    public static void main(String[] args) {
        System.out.println("Running power_of_four_342...");
    }
}
