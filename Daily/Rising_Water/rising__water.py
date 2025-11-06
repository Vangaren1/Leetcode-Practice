from typing import Optional, List
from collections import defaultdict
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        h = [(grid[0][0], 0, 0)]
        visited = set()

        curr = 0
        while h:
            curr, y, x = heapq.heappop(h)
            if (y, x) == (height - 1, width - 1):
                return curr
            if (y, x) in visited:
                continue
            visited.add((y, x))
            for dy, dx in diff:
                ny, nx = y + dy, x + dx
                if 0 <= ny < height and 0 <= nx < width and (ny, nx) not in visited:
                    cost = max(curr, grid[ny][nx])
                    heapq.heappush(h, (cost, ny, nx))

        return curr


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6],
    ]
    print(sol.swimInWater(grid))
    print("Running Solution...")
