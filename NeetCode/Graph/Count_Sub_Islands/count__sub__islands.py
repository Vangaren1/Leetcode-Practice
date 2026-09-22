from typing import Optional, List
import heapq
from collections import defaultdict, deque


class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        height = len(grid1)
        width = len(grid1[0])
        diff = ((0, 1), (0, -1), (1, 0), (-1, 0))

        count = 0

        def bfs(pos):

            dq = deque()
            dq.append(pos)

            y, x = pos
            grid2[y][x] = 0

            overlapped = True
            if grid1[y][x] == 0:
                overlapped = False

            while dq:
                y, x = dq.popleft()
                for dy, dx in diff:
                    ny, nx = dy + y, dx + x
                    if 0 <= ny < height and 0 <= nx < width and grid2[ny][nx] == 1:
                        if grid1[ny][nx] == 0:
                            overlapped = False
                        grid2[ny][nx] = 0
                        dq.append((ny, nx))
            return overlapped

        for y in range(height):
            for x in range(width):
                if grid2[y][x] == 1 and bfs((y, x)):
                    count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    grid1 = [
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
    ]
    grid2 = [
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0],
    ]
    print(sol.countSubIslands(grid1, grid2))
    print("Running Solution...")
