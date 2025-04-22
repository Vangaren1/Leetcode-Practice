package Grind75.week1.flood_fill_733;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int original = image[sr][sc];
        int[][] adj = {
            {1,0},
            {0,1},
            {-1,0},
            {0,-1}
        };

        Queue<int[]> queue = new LinkedList<>();
        Set<int[]> changed = new HashSet<>();

        queue.add(new int[] {sr,sc});


        while(!queue.isEmpty()){
            int[] curr = queue.poll();
            int row = curr[0];
            int col = curr[1];

            image[row][col] = color;
            changed.add(new int[] {row,col});

            for(int[] c : adj){
                if( 0 <= c[0] 
                    && c[0] < image.length - 1
                    && 0 <= c[1]
                    && c[1] < image[0].length - 1 
                    && image[c[0]][c[1]] == original){
                        queue.add(new int[] {c[0], c[1]});
                }
            }
        }

        return image;
    }
    public static void main(String[] args) {
        Solution s = new Solution();

        int [][] image = {{1,1,1},{1,1,0},{1,0,1}};
        int sr = 1 ;
        int sc = 1;
        int color = 2;

        s.floodFill(image, sr, sc, color);

        System.out.println("Running flood_fill_733...");
    }
}
