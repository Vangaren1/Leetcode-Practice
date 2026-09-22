from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        counted = set()
        height = len(grid)
        width = len(grid[0])

        for y in range(height):
            tmpset = set()
            for x in range(width):
                if grid[y][x] == 1:
                    tmpset.add((y, x))
            if len(tmpset) >= 2:
                for pos in tmpset:
                    counted.add(pos)

        for x in range(width):
            tmpset = set()
            for y in range(height):
                if grid[y][x] == 1:
                    tmpset.add((y, x))
            if len(tmpset) >= 2:
                for pos in tmpset:
                    counted.add(pos)

        return len(counted)
        pass


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
    ]
    print(sol.countServers(grid))
    print("Running Solution...")
