from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        dp = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

        dp[height - 1][width - 1] = 1
        for y in range(height - 1, -1, -1):
            for x in range(width - 1, -1, -1):
                if obstacleGrid[y][x] == 1:
                    continue
                dp[y][x] += dp[y + 1][x] + dp[y][x + 1]

        return dp[0][0]


if __name__ == "__main__":
    sol = Solution()
    obstacleGrid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 1, 0],
    ]
    print(sol.uniquePathsWithObstacles(obstacleGrid))
    print("Running Solution...")
