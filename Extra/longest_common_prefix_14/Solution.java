package Extra.longest_common_prefix_14;

class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = "";
        if (strs.length == 1){
            return strs[0];
        }
        int minlength = strs[0].length();
        for ( String str : strs){
            if ( str.length() < minlength){
                minlength = str.length();
            }
        }
        if (minlength < 1){
            return prefix;
        }
        for ( int index = 0; index < minlength; index ++){
            char tmp = strs[0].charAt(index);
            String curr = "";
            for ( String s : strs){
                curr = new String(s);
                if (s.charAt(index) != tmp){
                    prefix = s.substring(0, index);
                    return prefix;
                }
            }
            prefix = curr.substring(0,index + 1);
        }
        return prefix;
    }
    public static void main(String[] args) {
        String[] strs = {"ab","a"};

        Solution s = new Solution();
        System.out.println(s.longestCommonPrefix(strs));
        System.out.println("Running longest_common_prefix_14...");
    }
}
