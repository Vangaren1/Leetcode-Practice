package Grind75.week3.matrix_524;

import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    class Pair{
        int x,y;
        Pair(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

    public int[][] updateMatrix(int[][] mat) {
        int height = mat.length;
        int width = mat[0].length;

        Queue<Pair> queue = new ArrayDeque<>();

        for( int i = 0; i < height; i++){
            for( int j = 0; j < width; j++){
                if(mat[i][j] == 0){
                    queue.add(new Pair(j,i));
                }else{
                    mat[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        Pair[] diff  = {new Pair(0,1), new Pair(0,-1), new Pair(1,0), new Pair(-1,0)};


        while(!queue.isEmpty()){
            Pair curr = queue.poll();

            for(Pair d: diff){
                int nx = d.x + curr.x;
                int ny = d.y + curr.y;
                if( 0<= nx && nx < width && 0<=ny && ny < height){
                    if( mat[ny][nx] == Integer.MAX_VALUE){
                        mat[ny][nx] = mat[curr.y][curr.x] + 1;
                        queue.add(new Pair(nx,ny));
                    }else{
                        mat[ny][nx] = Math.min(mat[ny][nx], mat[curr.y][curr.x]+1);
                    }

                }
            }
        }


        return mat;
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        int[][] mat = {{0},{1}};
        mat = s.updateMatrix(mat);
        System.out.println("Running 01_matrix_524...");
    }
}
