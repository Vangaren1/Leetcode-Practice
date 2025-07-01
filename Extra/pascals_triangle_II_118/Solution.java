package Extra.pascals_triangle_II_118;

import java.util.ArrayList;
import java.util.List;

class Solution {

    public List<Integer> getRow(int rowIndex) {
        List<Integer> retRow = new ArrayList<>();
        retRow.add(1);
        if (rowIndex==0) return retRow;

        retRow.add(1);
        if (rowIndex==1) return retRow;

        retRow.remove(1);
        List<Integer> lastRow = getRow( rowIndex - 1);

        for ( int index = 0; index < lastRow.size() -1 ; index ++ ) {
            int newNum = lastRow.get(index) + lastRow.get(index + 1);
            retRow.add(newNum);
        }
        retRow.add(1);
        return retRow;
    }
    
    public static void main(String[] args) {
        System.out.println("Running pascals_triangle_II_118...");
    }
}
