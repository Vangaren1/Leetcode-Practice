from typing import Optional, List
import heapq
from collections import defaultdict, deque


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        diff = ((0, 1), (0, -1), (1, 0), (-1, 0))

        maxFish = 0

        def bfs(pos):

            visited = set()
            visited.add((pos))
            total = 0

            dq = deque()
            dq.append(pos)

            while dq:
                y, x = dq.popleft()

                total += grid[y][x]
                grid[y][x] = 0

                for dy, dx in diff:
                    ny, nx = dy + y, dx + x
                    if (
                        0 <= ny < height
                        and 0 <= nx < width
                        and grid[ny][nx] != 0
                        and (ny, nx) not in visited
                    ):
                        visited.add((ny, nx))
                        dq.append((ny, nx))
            return total

        for y in range(height):
            for x in range(width):
                if grid[y][x] != 0:
                    maxFish = max(maxFish, bfs((y, x)))
        return maxFish


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [0, 2, 1, 0],
        [4, 0, 0, 3],
        [1, 0, 0, 4],
        [0, 3, 2, 0],
    ]
    print(sol.findMaxFish(grid))
    print("Running Solution...")
