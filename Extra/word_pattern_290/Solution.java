package Extra.word_pattern_290;

class Solution {
    public boolean isPowerOfThree(int n) {
        if ( n <= 0) return false;
        while ( n % 3 == 0){
            n = n / 3;
        }
        return n == 1;
    }
    public static void main(String[] args) {
        System.out.println("Running word_pattern_290...");
    }
}
