package Extra.pascals_triangle_118;

import java.util.ArrayList;
import java.util.List;

class Solution {

    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> baseCase = new ArrayList<>();
        if ( numRows == 0) return baseCase;
        
        List<Integer> one = new ArrayList<>();
        one.add(1);
        baseCase.add(new ArrayList<>(one));
        if (numRows == 1) return baseCase;
    
        List<Integer> two = new ArrayList<>(one);
        two.add(1);
        baseCase.add(two);
        if ( numRows == 2) return baseCase;
        
        List<List<Integer>> retList = generate(numRows -1 );

        List<Integer> lastRow = retList.get(retList.size()-1);

        List<Integer> newRow = new ArrayList<>();
        newRow.add(1);

        for ( int index = 0; index < lastRow.size() -1 ; index ++ ){
            int newNum = lastRow.get(index) + lastRow.get(index+1);
            newRow.add(newNum);
        }
        newRow.add(1);
        retList.add(newRow);
        return retList;


    }
    public static void main(String[] args) {
        System.out.println("Running pascals_triangle_118...");
    }
}
