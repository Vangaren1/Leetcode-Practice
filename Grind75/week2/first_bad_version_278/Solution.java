package Grind75.week2.first_bad_version_278;



public class Solution extends VersionControl {

    public int firstBadVersion(int n) {
        int start = 0;
        int end = n;
        int mid = (int)(((long)start + (long)end ) /2 );
        while(start <= end){
            Boolean check = isBadVersion(mid);
            if(!check){
                start = mid + 1;
            }else{
                if(!isBadVersion(mid-1)){
                    return mid;
                }
                end = mid;
            }
            mid = (int)(((long)start + (long)end ) /2 );
        }
        return 0;
    }
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(2126753390 + 1702766719);

        System.out.println(s.firstBadVersion(2126753390));

        System.out.println("Running first_bad_version_278...");
    }
}
