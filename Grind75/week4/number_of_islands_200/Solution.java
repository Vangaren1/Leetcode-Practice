package Grind75.week4.number_of_islands_200;
import common.Node;

class Solution {
    int height; 
    int width; 
    char[][] islands;

    public int numIslands(char[][] grid) {
        height = grid.length;
        width = grid[0].length;
        islands = grid;

        int found = 0;
        for ( int i = 0; i < height ; i++ ){
            for ( int j = 0; j < width; j ++){
                if ( islands[i][j] == '1'){
                    dfs(i, j);
                    found++;
                }
            }
        }

        return found;    
    }

    public void dfs(int y, int x){
        if ( y < 0 || x < 0 || y >= height || x >= width || islands[y][x] == '0'){
            return;
        }else{
            islands[y][x] = '0';
            dfs( y + 1, x);
            dfs( y - 1, x);
            dfs( y, x+1);
            dfs( y, x-1);
        }
    }
    public static void main(String[] args) {
        Solution sol = new Solution();

        char[][] grid = {{'1','1','1', '1','0'}, {'1','1','0', '0','0'}, {'1','1','0', '0','0'}, {'1','0','0', '0','0'}};

        int results = sol.numIslands(grid);
        System.out.println(results);

        System.out.println("Running number_of_islands_200...");
    }
}
