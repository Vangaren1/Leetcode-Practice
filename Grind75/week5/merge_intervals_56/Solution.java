package Grind75.week5.merge_intervals_56;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[][] merge(int[][] intervals) {
        List<List<Integer>> res = new ArrayList<>();

        Arrays.sort( intervals, (a,b) -> Integer.compare(a[0], b[0]));

        int curr = 0;

        for ( int[] inter : intervals){
            // if empty, just add the first one
            if ( res.size() == 0){
                res.add( intToList(inter));
            }else{
                // compare the element to the one currently in the list
                List<Integer> tmp = res.get(curr);
                if( overlap( tmp, inter)){
                    tmp.set(0, Integer.min(tmp.get(0), inter[0]));
                    tmp.set(1, Integer.max(tmp.get(1), inter[1]));
                    res.set(curr, tmp);
                }else{
                    res.add(intToList(inter));
                    curr++;
                }
            }
        }

        int[][] returnList = new int[res.size()][2];
        int index = 0;
        for ( List<Integer> interval : res){
            returnList[index][0] = interval.get(0);
            returnList[index][1] = interval.get(1);
            index++;    
        }

        return returnList;
    }

    public boolean overlap(List<Integer> a, int[] b){
        if ( a.get(1) >= b[0] || a.get(1) >= b[1] ){
            return true;
        }
        if( a.get(0) >= b[1] || a.get(0) >= b[0]){
            return true;
        }
        return false;
    }

    public List<Integer> intToList(int[] a){
        List<Integer> tmp = new ArrayList<>();
        tmp.add(a[0]);
        tmp.add(a[1]);
        return tmp;
    }

    public int[] convert(List<Integer> inter){
        int[] ret = new int[2];
        ret[0] = inter.get(0);
        ret[1] = inter.get(1);
        return ret; 
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        int[][] intervals = {{1,3},{2,6},{8,10},{15,18}};

        int[][] inter2 = {{1,4}, {0,0}};

        System.out.println(s.merge(intervals));

        System.out.println("Running merge_intervals_56...");
    }
}
