from typing import Optional, List
import heapq
from collections import defaultdict, deque


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        islands = defaultdict(int)
        islandCounter = 2
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def bfs(pos, islandCount):
            thisIsland = set()
            thisIsland.add(pos)
            dq = deque()
            dq.append(pos)
            grid[pos[0]][pos[1]] = islandCount
            islands[islandCount] += 1
            while dq:
                curr = dq.popleft()

                y, x = curr

                for dy, dx in diff:
                    ny, nx = dy + y, dx + x
                    if (
                        ny < 0
                        or nx < 0
                        or ny >= height
                        or nx >= width
                        or grid[ny][nx] == 0
                        or (ny, nx) in thisIsland
                    ):
                        continue
                    islands[islandCount] += 1
                    thisIsland.add((ny, nx))
                    dq.append((ny, nx))
                    grid[ny][nx] = islandCount

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    bfs((y, x), islandCounter)
                    islandCounter += 1

        if islandCounter - 2 == 0:
            return 1

        best = 0

        foundZero = False
        for y in range(height):
            for x in range(width):
                nextTo = 0
                if grid[y][x] == 0:
                    foundZero = True
                    seen = set()
                    for dy, dx in diff:
                        ny, nx = dy + y, dx + x
                        if (
                            ny < 0
                            or nx < 0
                            or ny >= height
                            or nx >= width
                            or grid[ny][nx] == 0
                            or grid[ny][nx] in seen
                        ):
                            continue
                        seen.add(grid[ny][nx])
                        nextTo += islands[grid[ny][nx]]

                    best = max(best, nextTo + 1)

        if not foundZero:
            return height * width

        return best


if __name__ == "__main__":
    sol = Solution()
    # grid = [
    #     [0, 0],
    #     [0, 0],
    # ]
    # print(sol.largestIsland(grid))
    # grid = [
    #     [1, 1],
    #     [1, 1],
    # ]
    # print(sol.largestIsland(grid))
    # grid = [
    #     [1, 0],
    #     [0, 1],
    # ]
    # print(sol.largestIsland(grid))
    grid = [
        [1, 0],
        [1, 1],
    ]
    print(sol.largestIsland(grid))
    # grid = [
    #     [1, 0, 0],
    #     [0, 1, 1],
    #     [0, 1, 1],
    # ]
    # print(sol.largestIsland(grid))
    print("Running Solution...")
