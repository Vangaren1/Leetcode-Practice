package Extra.excel_column_number_171;

class Solution {
    public int titleToNumber(String columnTitle) {
        int total = 0;
        
        for ( char c : columnTitle.toCharArray() ){
            int thisC = (c - 'A') + 1;
            total = total * 26;
            total = total + thisC;
        }
        return total;
    }
    public static void main(String[] args) {
        String test = "AB";
        Solution s = new Solution();
        System.out.println(s.titleToNumber(test));
        System.out.println("Running excel_column_number_171...");
    }
}
