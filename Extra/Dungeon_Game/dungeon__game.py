from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        height = len(dungeon)
        width = len(dungeon[0])
        dp = [[float("inf") for _ in range(width + 1)] for _ in range(height + 1)]

        dp[height][width - 1] = 1
        dp[height - 1][width] = 1

        for y in range(height - 1, -1, -1):
            for x in range(width - 1, -1, -1):
                need = min(dp[y + 1][x], dp[y][x + 1])
                dp[y][x] = max(1, need - dungeon[y][x])
        return dp[0][0]


if __name__ == "__main__":
    sol = Solution()
    dungeon = [[0, -3]]
    print(sol.calculateMinimumHP(dungeon))
    print("Running Solution...")
