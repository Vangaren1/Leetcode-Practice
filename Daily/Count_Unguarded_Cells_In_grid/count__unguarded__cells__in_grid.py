from typing import Optional, List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        width = n
        height = m
        total = m * n

        wallset = set([(y, x) for y, x in walls])
        total -= len(walls)

        guardSet = set([(y, x) for y, x in guards])
        total -= len(guards)

        seen = set()

        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for y, x in guards:

            for dy, dx in diff:
                ny, nx = y + dy, x + dx
                while (
                    0 <= ny < height
                    and 0 <= nx < width
                    and (ny, nx) not in wallset
                    and (ny, nx) not in guardSet
                ):
                    if (ny, nx) not in seen:
                        total -= 1
                        seen.add((ny, nx))
                    ny, nx = ny + dy, nx + dx

        return total


if __name__ == "__main__":
    sol = Solution()
    m = 2
    n = 7
    guards = [[1, 5], [1, 1], [1, 6], [0, 2]]
    walls = [[0, 6], [0, 3], [0, 5]]
    print(sol.countUnguarded(m, n, guards, walls))
    print("Running Solution...")


"""

Works but times out at test case 38/49

class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        width = n
        height = m
        total = m * n
        grid = [[0] * width for _ in range(height)]

        for y, x in walls:
            grid[y][x] = 2
            total -= 1

        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for y, x in guards:
            if grid[y][x] == 0:
                total -= 1
            grid[y][x] = 1

            for dy, dx in diff:
                ny, nx = y + dy, x + dx
                while 0 <= ny < height and 0 <= nx < width and grid[ny][nx] != 2:
                    if grid[ny][nx] == 0:
                        total -= 1
                        grid[ny][nx] = 3
                    ny, nx = ny + dy, nx + dx

        for row in grid:
            print(row)

        return total
        
"""
