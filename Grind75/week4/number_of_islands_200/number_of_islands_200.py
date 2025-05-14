from typing import Optional, List

from common.graphnode import GraphNode as Node, print_graph_bfs, build_graph

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
       
        def dfs(y,x):
            if y < 0 or y >= height or x < 0 or x >= width or grid[y][x] == '0':
                return
            grid[y][x] = '0'
            for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
                ny = dy + y
                nx = dx + x
                dfs(ny,nx)
        
        currCount = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == '1':
                    dfs(y,x)      
                    currCount += 1
        
        return currCount

if __name__ == "__main__":
    grid = [    ["1","1","1","1","0"],  
                ["1","1","0","1","0"],  
                ["1","1","0","0","1"], 
                ["0","0","1","1","0"] ]
    
    s= Solution()
    print("Number of islands found")
    print(s.numIslands(grid))
    
    print("Running Solution...")
