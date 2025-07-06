package Grind75.week7.minimum_height_tree_310;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<Integer> retVal = new ArrayList<>();
        if (n==1) {
            retVal.add(0);
            return retVal;
        }
        Map<Integer,List<Integer>> adj = new HashMap<>();
        for ( int[] edge : edges) {
            if( adj.containsKey(edge[0])){
                adj.get(edge[0]).add(edge[1]);
            } else{
                adj.put(edge[0], new ArrayList<>());
                adj.get(edge[0]).add(edge[1]);
            }
            if( adj.containsKey(edge[1])){
                adj.get(edge[1]).add(edge[0]);
            } else{
                adj.put(edge[1], new ArrayList<>());
                adj.get(edge[1]).add(edge[0]);
            }
        }

        Map<Integer, Integer> edgeCount = new HashMap<>();
        Deque<Integer> leaf = new ArrayDeque<>();
        for ( int src : adj.keySet()) {
            List<Integer> tmp = adj.get(src);
            if ( tmp.size() == 1) {
                leaf.add(src);
            }
            edgeCount.put(src, tmp.size());
        }

        while ( !leaf.isEmpty()) {
            if ( n <= 2){
                break;
            }
            int leafSize = leaf.size();
            for ( int index = 0; index < leafSize; index ++){
                int node = leaf.removeFirst();
                n--;
                for ( int nei : adj.get(node)) {
                    edgeCount.put(nei, edgeCount.get(nei) - 1);
                    if ( edgeCount.get(nei) == 1) leaf.add(nei);
                }
            }
        }

        return new ArrayList<>(leaf);
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        int n = 4;
        int edges[][] = {{1,0},{1,2},{1,3}};

        System.out.println(s.findMinHeightTrees(n, edges));
        System.out.println("Running minimum_height_tree_310...");
    }
}
