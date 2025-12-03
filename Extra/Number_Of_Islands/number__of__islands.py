from typing import Optional, List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))

        count = 0

        def bfs(a, b):
            queue = deque()
            queue.append((a, b))

            while queue:
                y, x = queue.popleft()
                grid[y][x] = count

                for dy, dx in diff:
                    ny, nx = dy + y, dx + x
                    if (
                        0 <= ny < height
                        and 0 <= nx < width
                        and grid[ny][nx] == "1"
                        and (ny, nx) not in queue
                    ):
                        queue.append((ny, nx))

        for h in range(height):
            for w in range(width):
                if grid[h][w] == "1":
                    count += 1
                    bfs(h, w)
        return count

        pass


if __name__ == "__main__":
    sol = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "1", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(sol.numIslands(grid))
    print("Running Solution...")
