from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        count = 0

        dp = [[[0, False] for _ in range(width + 1)] for _ in range(height + 1)]
        costMap = {"X": 1, "Y": -1, ".": 0}
        for y in range(1, height + 1):
            for x in range(1, width + 1):
                tmp = grid[y - 1][x - 1]
                dp[y][x][0] = (
                    costMap[tmp]
                    + dp[y - 1][x][0]
                    + dp[y][x - 1][0]
                    - dp[y - 1][x - 1][0]
                )
                if tmp == "X" or dp[y - 1][x][1] or dp[y][x - 1][1]:
                    dp[y][x][1] = True
                if dp[y][x][0] == 0 and dp[y][x][1]:
                    count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    grid = [[".", "."], [".", "."]]
    print(sol.numberOfSubmatrices(grid))
    print("Running Solution...")
