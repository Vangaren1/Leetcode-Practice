package Grind75.week4.course_schedule_207;

import common.Node;
import java.util.List;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

class Solution {

    List<List<Integer>> courseList = new ArrayList<>();
    Set<Integer> seen = new HashSet<>();
    Set<Integer> complete = new HashSet<>();

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        
        for(int i=0; i < numCourses; i++){
            courseList.add(new ArrayList<>());
        }
        for(int[] req: prerequisites){
            courseList.get(req[0]).add(req[1]);
        }

        for(int j = 0; j< numCourses; j++){
            if(dfs(j)){
                return false;
            }
        }

        return true;
    }

    private boolean dfs(int course){
        if(!complete.contains(course)){
            complete.add(course);
            seen.add(course);
            for(int req: courseList.get(course)){
                if(dfs(req) && !complete.contains(req)){
                    return true;
                }else if(seen.contains(req)){
                    return true;
                }
            }
            seen.remove(course);
        }

        return false;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[][] prereq = {{1,0}};
        System.out.println(s.canFinish(2, prereq));
        System.out.println("Running course_schedule_207...");
    }
}
