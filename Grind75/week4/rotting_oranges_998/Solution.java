package Grind75.week4.rotting_oranges_998;
// import common.Node;

import java.util.ArrayDeque;
import java.util.Queue;

class Solution {

    public int orangesRotting(int[][] grid) {
        int time = 0;
        int height = grid.length;
        int width = grid[0].length;
        int oranges = 0;

        Queue<int[]> q = new ArrayDeque<>();

        int[][] directions = {
            {0, 1},
            {0, -1},
            {1, 0}, 
            {-1, 0}  
        };

        for(int y = 0; y < height; y++){
            for( int x = 0; x < width; x++){
                if( grid[y][x] == 2){
                    q.add(new int[] {y,x});
                } else if ( grid[y][x] == 1){
                    oranges++;
                }
            }
        }

        int sizeofqueue = 0;
        int ny = 0;
        int nx = 0;
        int[] tmp = {0,0};

        while( !q.isEmpty() && oranges > 0){
            sizeofqueue = q.size();
            for ( int i = 0; i < sizeofqueue; i++ ){
                tmp = q.poll();
                for( int[] dir : directions){
                    ny = dir[0] + tmp[0];
                    nx = dir[1] + tmp[1];
                    if ( ny < 0 || ny >= height || nx < 0 || nx >= width || grid[ny][nx] != 1){
                        continue;
                    }else{
                        q.add(new int[]{ny,nx});
                        grid[ny][nx]=2;
                        oranges--;
                    }
                }
            }
            time++;
        }
        if (oranges > 0){
            return -1;
        }
        return time;
    }

    public static void main(String[] args) {
        System.out.println("Running rotting_oranges_998...");
    }
}
