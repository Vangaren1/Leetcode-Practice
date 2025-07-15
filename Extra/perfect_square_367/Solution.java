package Extra.perfect_square_367;

class Solution {
    public boolean isPerfectSquare(int num) {
        if ( num < 0 ) return false;
        if ( num == 1 || num == 0) return true;

        long left = 0;
        long right = num /2;
        
        long mid = (left + right) / 2;

        while ( left <= right) {
            long curr = mid * mid;
            if ( curr == num) return true;

            if ( curr < num){
                left = mid + 1;
            } else {
                right = mid - 1;
            }
            
            mid = (left + right) /2;

        }
        
        return false;
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        int n = 808201;
        System.out.println(s.isPerfectSquare(n));
        System.out.println("Running perfect_square_367...");
    }
}
