package Grind75.week7.task_scheduler_621;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int leastInterval(char[] tasks, int n) {

        Map<Character, Integer> taskDict = new HashMap<>();
        for (int index = 0; index < tasks.length; index++ ) {
            taskDict.merge(tasks[index], 1,Integer::sum);
        }
        
        return 0;
    }
    public static void main(String[] args) {
        System.out.println("Running task_scheduler_621...");
    }
}
