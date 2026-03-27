from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        height = len(grid)
        width = len(grid[0])

        dp = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

        for y in range(1, height + 1):
            for x in range(1, width + 1):
                dp[y][x] = (
                    dp[y - 1][x] + dp[y][x - 1] + grid[y - 1][x - 1] - dp[y - 1][x - 1]
                )

        lastVal = dp[height][width] // 2
        if lastVal % 2 == 1:
            return False
        for y in range(1, height + 1):
            if dp[y][width] == (lastVal):
                return True
        for x in range(1, width + 1):
            if dp[height][x] == (lastVal):
                return True
        return False


if __name__ == "__main__":
    sol = Solution()

    grid = [[1, 1, 1]]
    print(sol.canPartitionGrid(grid))

    print("Running Solution...")
