package Extra.excel_column_title_168;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder sb = new StringBuilder();

        while ( columnNumber > 0) {
            columnNumber--;
            int digit = columnNumber % 26;
            char c = (char) ('A' + digit);
            sb.insert(0,c);
            columnNumber = columnNumber / 26;
        }
           
        return sb.toString();
    }
    public static void main(String[] args) {
        System.out.println("Running excel_column_title_168...");
    }
}
