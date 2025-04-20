
class Solution {

    public boolean isPalindrome(String s) {
        
        int head = 0;
        int tail = s.length() - 1;
        
        while(head < tail){
            while(!Character.isLetterOrDigit(s.charAt(head)) ){
                head++;
                continue;
            }
            while(!Character.isLetterOrDigit(s.charAt(tail))){
                tail--;
                continue;
            }
            char cHead = Character.toLowerCase(s.charAt(head));
            char cTail = Character.toLowerCase(s.charAt(tail));
            if(cHead != cTail){
                return false;
            }
            head++;
            tail--;
        }

        return true;
    }
    public static void main(String[] args) {
        String test = "A man, a plan, a canal: Panama";

        Solution s = new Solution();

        s.isPalindrome(test);

        System.out.println("Running valid_palindrone-125...");
    }
}
