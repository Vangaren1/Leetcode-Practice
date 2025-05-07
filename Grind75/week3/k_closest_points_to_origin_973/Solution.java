package Grind75.week3.k_closest_points_to_origin_973;

import java.util.ArrayList;
import java.util.PriorityQueue;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Coord> queue = new PriorityQueue<>();

        for(int[] p: points){
            queue.add(new Coord(p[0], p[1]));
        }

        ArrayList<int[]> results = new ArrayList<>();

        while(k > 0){
            Coord tmp = queue.poll();
            results.add( tmp.getPair() );
            k--;
        }

        return results.toArray(new int[results.size()][]);   
    }

    class Coord implements Comparable<Coord> {

        int distance;
        int x, y;

        public Coord(int x, int y){
            this.x = x;
            this.y = y;
            this.distance = x*x + y*y;
        }

        public int[] getPair(){
            return new int[] {this.x, this.y};
        }

        @Override
        public int compareTo(Coord other) {
            return Integer.compare(this.distance, other.distance);
        }
    }

    public static void main(String[] args) {
        int[][] points = {{3,3},{5,-1},{-2,4}};
        int k = 2;

        Solution s = new Solution();
        System.out.println(s.kClosest(points, k));
        System.out.println("Running k_closest_points_to_origin_973...");
    }
}
