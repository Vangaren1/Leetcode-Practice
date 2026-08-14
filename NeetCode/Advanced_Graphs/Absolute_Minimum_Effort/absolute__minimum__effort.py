from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        height = len(heights)
        width = len(heights[0])
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        dist = [[float("inf") for _ in range(width)] for _ in range(height)]
        dist[0][0] = 0
        queue = [(0, 0, 0)]

        while queue:
            effort_so_far, y, x = heapq.heappop(queue)

            if effort_so_far > dist[y][x]:
                continue

            currHeight = heights[y][x]

            for dy, dx in diff:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < height and 0 <= nx < width:
                    stepDiff = abs(currHeight - heights[ny][nx])
                    newEffort = max(effort_so_far, stepDiff)
                    if newEffort < dist[ny][nx]:
                        dist[ny][nx] = newEffort
                        heapq.heappush(queue, (newEffort, ny, nx))
        return dist[height - 1][width - 1]


if __name__ == "__main__":
    sol = Solution()

    heights = [
        [1, 1, 1],
        [3, 2, 4],
        [2, 5, 4],
    ]
    print(sol.minimumEffortPath(heights))
    print("Running Solution...")
