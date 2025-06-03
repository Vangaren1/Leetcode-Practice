from typing import Optional, List

from common.graphnode import GraphNode as Node, print_graph_bfs, build_graph

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        rotten = []
        visited = set()
        
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 2:
                    rotten.append((y,x))
                elif grid[y][x] == 1:
                    visited.add((y,x))
                    grid[y][x] = float('inf')
            
        inProcess = set()
        def dfs(y,x, depth):
            nonlocal inProcess
            if grid[y][x] <= 0 or 0 > y  or y >= height or 0 > x or x >= width:
                return 
            inProcess.add((y,x))
            grid[y][x] = min(grid[y][x], depth)
            for dy, dx in ((1,0), (-1, 0), (0,1), (0,-1)):
                ny = dy + y
                nx = dx + x
                if 0 <= ny < height and 0 <= nx  < width and (ny, nx) not in rotten and (ny,nx) not in inProcess and grid[ny][nx] != 0: 
                    dfs(ny, nx, depth + 1)
            if (y,x) in visited:
                visited.remove((y,x))
            inProcess.remove((y,x))
                    
        for y,x in rotten:
            dfs(y,x, 0)
        
        if len(visited) > 0:
            return -1
        
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
