package Grind75.week3.insert_interval_57;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> results = new ArrayList<>();
        List<int[]> inter = new ArrayList<>(Arrays.asList(intervals));

        for(int ptr = 0; ptr < intervals.length; ptr ++){
            if( newInterval[1] < intervals[ptr][0]){
                results.add(newInterval);
                results.addAll(inter.subList(ptr, inter.size()));
                return results.toArray(new int[0][]);
            } else if(intervals[ptr][1] < newInterval[0]){
                results.add(intervals[ptr]);
            }else{
                newInterval[0] = Math.min(newInterval[0], intervals[ptr][0]);
                newInterval[0] = Math.max(newInterval[1], intervals[ptr][1]);
            }
        }
        results.add(newInterval);
        return results.toArray(new int[0][]);
    }
    public static void main(String[] args) {
        System.out.println("Running insert_interval_57...");
    }
}
