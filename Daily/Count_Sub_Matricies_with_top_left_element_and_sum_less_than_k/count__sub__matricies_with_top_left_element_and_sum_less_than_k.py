from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        height = len(grid)
        width = len(grid[0])

        dp = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

        count = 0
        for y in range(1, height + 1):
            for x in range(1, width + 1):
                dp[y][x] = (
                    grid[y - 1][x - 1] + dp[y - 1][x] + dp[y][x - 1] - dp[y - 1][x - 1]
                )
                if dp[y][x] <= k:
                    count += 1

        return count


if __name__ == "__main__":
    sol = Solution()
    grid = [[7, 2, 9], [1, 5, 0], [2, 6, 6]]
    k = 20
    print(sol.countSubmatrices(grid, k))

    grid = [[7, 6, 3], [6, 6, 1]]
    k = 18
    print(sol.countSubmatrices(grid, k))
    print("Running Solution...")
