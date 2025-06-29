package Extra.sqrt_69;

class Solution {
    public int mySqrt(int x) {
        if (x < 2){
            return x;
        }

        long left = 1;
        long right = x / 2;
        long mid = ( left + right ) /2 ;
        while ( left <= right){
            long curr = mid * mid;
            long cnext = (mid + 1) * (mid + 1);
            if ( curr == x) return (int)mid;
            if (curr < x && cnext > x) {
                return (int) mid;
            }
            if ( curr > x ) {
                right = mid -1;
            } else{
                left = mid + 1;
            }
            mid = (left + right) /2 ;

        }
        return (int) mid;
    }

    
    public static void main(String[] args) {
        int x = 2147395599;
        Solution s = new Solution();

        System.out.println(s.mySqrt(x));
        System.out.println("Running sqrt_69...");
    }
}
