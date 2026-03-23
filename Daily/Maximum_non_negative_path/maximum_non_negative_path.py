from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        dp = [[[0, 0] for _ in range(width)] for _ in range(height)]
        
        y,x = 0,0

        while y != height - 1 and x != width -1:
            
            
        
        pass


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [1, -2, 1],
        [1, -2, 1],
        [3, -4, 1],
    ]
    print(sol.maxProductPath(grid))
    print("Running Solution...")
