from typing import Optional, List
from collections import deque

from common.graphnode import GraphNode as Node, print_graph_bfs, build_graph

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        q = deque()
        ocount = 0
        time = 0
        
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 2:
                    q.append((y,x))
                elif grid[y][x] == 1:
                    ocount += 1  
                
        diff = ((0,1),(0,-1),(1,0),(-1,0))
        
        while q and ocount > 0:
            
            for i in range(len(q)):
                y,x = q.pop()
                for dy, dx in diff:
                    ny, nx = dy + y , dx + x
                    if  (ny < 0 or ny == height or 
                         nx < 0 or nx == width or 
                         grid[ny][nx] != 1):
                        continue
                    q.appendleft((ny,nx))
                    grid[ny][nx] = 2
                    ocount -= 1
                    
            time += 1 
        return time if ocount == 0 else -1
                        
                
                
                

if __name__ == "__main__":
    s = Solution()
    
    grid = [[2,1,1],[1,1,1],[1,1,1]]
    expected = 4
    
    assert s.orangesRotting(grid) == expected
    
    print("Running Solution...")
