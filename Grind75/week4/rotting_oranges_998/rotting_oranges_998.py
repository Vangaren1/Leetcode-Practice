from typing import Optional, List

from common.graphnode import GraphNode as Node, print_graph_bfs, build_graph

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        rotten = []
        
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 2:
                    rotten.append((y,x))
                elif grid[y][x] == 1:
                    grid[y][x] = float('inf')
                    
        def dfs(y,x, depth):
            if 0 > y  or y >= height or 0 > x  or x >= width:
                return 
            grid[y][x] = min(grid[y][x], depth)
            for dy, dx in ((1,0), (-1, 0), (0,1), (0,-1)):
                ny = dy + y
                nx = dx + x
                if (ny, nx) not in rotten: 
                    dfs(ny, nx, depth + 1)
                    
        for y,x in rotten:
            dfs(y,x, 0)
        
        
        maxDepth = 0
        for y in range(height):
            for x in range(width):
                maxDepth = max(maxDepth, grid[y][x])
        
        return maxDepth 
                        
                
                
                

if __name__ == "__main__":
    s = Solution()
    
    grid = [[2,1,1],[1,1,1],[0,1,2]]
    expected = 4
    
    assert s.orangesRotting(grid) == expected
    
    print("Running Solution...")
