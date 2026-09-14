from typing import Optional, List
import heapq
from collections import defaultdict, deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))

        targetY, targetX = n - 1, n - 1

        if grid[0][0] == 1:
            return -1
        if grid[n - 1][n - 1] == 1:
            return -1

        def bfs(pos):
            seen = set()
            seen.add((0, 0))
            dq = deque()
            dq.append((1, pos))

            while dq:
                dist, (y, x) = dq.popleft()
                print(f"looking at y:{y}, x:{x}")
                for dy, dx in diff:
                    ny, nx = dy + y, dx + x

                    if targetY == ny and targetX == nx:
                        return dist + 1
                    if (
                        0 <= ny < n
                        and 0 <= nx < n
                        and grid[ny][nx] == 0
                        and (ny, nx) not in seen
                    ):
                        seen.add((ny, nx))
                        dq.append((dist + 1, (ny, nx)))

        dist = bfs((0, 0))

        if dist is None:
            return -1
        return dist

        pass


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [1, 1, 0],
    ]
    print(sol.shortestPathBinaryMatrix(grid))
    print("Running Solution...")
