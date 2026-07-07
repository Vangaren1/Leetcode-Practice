from typing import Optional, List
import heapq
from collections import defaultdict, deque


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        height = len(grid)
        width = len(grid[0])

        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        INF = float("inf")

        dist = [[INF] * width for _ in range(height)]
        dist[0][0] = grid[0][0]

        dq = deque([(0, 0)])

        while dq:
            y, x = dq.popleft()

            for dy, dx in diff:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < height and 0 <= nx < width):
                    continue

                cost = grid[ny][nx]
                totalCost = dist[y][x] + cost

                if totalCost > health:
                    continue

                if totalCost < dist[ny][nx]:
                    dist[ny][nx] = totalCost
                    if cost == 0:
                        dq.appendleft((ny, nx))
                    else:
                        dq.append((ny, nx))

        return dist[height - 1][width - 1] < health


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
    ]
    health = 1
    print(sol.findSafeWalk(grid, health))
    print("Running Solution...")
