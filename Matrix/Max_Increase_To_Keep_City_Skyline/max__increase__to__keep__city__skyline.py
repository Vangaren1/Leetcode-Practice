from typing import Optional, List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cols = [max([grid[x][y] for x in range(n)]) for y in range(n)]
        rows = [max([grid[y][x] for x in range(n)]) for y in range(n)]
        total = 0

        for y in range(n):
            for x in range(n):
                total += min(cols[y], rows[x]) - grid[y][x]
        return total


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [3, 0, 8, 4],
        [2, 4, 5, 7],
        [9, 2, 6, 3],
        [0, 3, 1, 0],
    ]

    print(sol.maxIncreaseKeepingSkyline(grid))
    print("Running Solution...")
