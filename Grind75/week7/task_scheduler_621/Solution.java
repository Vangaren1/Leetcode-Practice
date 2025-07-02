package Grind75.week7.task_scheduler_621;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    class Pair{
        int count, time;
        public Pair(int count, int time){
            this.count = count;
            this.time = time;
        }
    }
    public int leastInterval(char[] tasks, int n) {

        Map<Character, Integer> taskDict = new HashMap<>();
        for (int index = 0; index < tasks.length; index++ ) {
            taskDict.merge(tasks[index], 1,Integer::sum);
        }
        
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
        for ( int c : taskDict.values()) {
            maxHeap.add(-c);
        }

        Deque<Pair> qu = new ArrayDeque<>();

        int time = 0;

        while (!maxHeap.isEmpty() || !qu.isEmpty()) {
            time++;
            if ( !maxHeap.isEmpty()) {
                int cnt = 1 + maxHeap.poll();
                if ( cnt < 0){
                    qu.add(new Pair(cnt, time + n));
                }
            }
            if ( !qu.isEmpty() && qu.peek().time == time) {
                maxHeap.add( qu.pollFirst().count );
            }
            
        }
        return time;
    }
    public static void main(String[] args) {

        Solution s = new Solution();

        String test = "AAABBB";

        System.out.println(s.leastInterval(test.toCharArray(), 2));



        System.out.println("Running task_scheduler_621...");
    }
}
