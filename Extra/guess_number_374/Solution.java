package Extra.guess_number_374;

class Solution {
    public int guessNumber(int n) {
        long left = 0;
        long right = n;
        right++;
        long curr = n / 2;

        int check = guess( (int)curr);
        while ( check != 0 && left < right) {
            if ( check == -1 ) {
                right = curr - 1;
            } else{
                left = curr + 1;
            }

            curr = (left + right )/2;
            check = guess((int)curr);
        }
        return (int)curr;
    }

    public int guess(int n) {
        int pick = 2147483647;
        if ( n == pick ) return 0;
        if ( n > pick) return -1;
        return 1;
    }
    public static void main(String[] args) {
        int n = 2147483647;
        Solution s = new Solution();
        System.out.println(s.guessNumber(n));
        System.out.println("Running guess_number_374...");
    }
}
