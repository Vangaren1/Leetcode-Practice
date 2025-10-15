from typing import Optional, List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)

        seen = set()
        for index in range(n):
            if grid[index][index] == 0 or grid[index][n - index - 1] == 0:
                return False
            seen.add((index, index))
            seen.add((index, n - index - 1))
        for y in range(n):
            for x in range(n):
                if (y, x) not in seen and grid[y][x] != 0:
                    return False
        return True


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [2, 0, 0, 1],
        [0, 3, 1, 0],
        [0, 5, 2, 0],
        [4, 0, 0, 0],
    ]
    print(sol.checkXMatrix(grid))
    print("Running Solution...")
