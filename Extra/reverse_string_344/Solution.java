package Extra.reverse_string_344;

class Solution {
    public void reverseString(char[] s) {
        char tmp; 

        int first=0;
        int last = s.length-1;
        while (first<last){
            tmp = s[first];
            s[first] = s[last];
            s[last] = tmp;
            first++;
            last--;
        }
        
    }
    public static void main(String[] args) {
        char[] s = "Hello".toCharArray();
        Solution sol = new Solution();
        sol.reverseString(s);
        System.out.println(new String(s));
        System.out.println("Running reverse_string_344...");
    }
}
