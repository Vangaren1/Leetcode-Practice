from typing import Optional, List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))

        queue = deque()
        count = 0
        # find the rotting oranges, store in queue with y, x, and time
        # count regular oranges
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 2:
                    queue.append((y, x, 0))
                if grid[y][x] == 1:
                    count += 1

        totalTime = 0

        while queue:
            y, x, time = queue.popleft()
            totalTime = time
            for dy, dx in diff:
                ny, nx = y + dy, x + dx
                if (
                    0 <= ny < height
                    and 0 <= nx < width
                    and grid[ny][nx] == 1
                    and (ny, nx) not in queue
                ):
                    grid[ny][nx] = 2
                    count -= 1
                    queue.append((ny, nx, time + 1))

        return totalTime if count == 0 else -1


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]
    expected = 4

    print(sol.orangesRotting(grid))
    print("Running Solution...")
