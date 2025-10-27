from typing import Optional, List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        dp = [[float("inf")] * width for _ in range(height)]

        for y in range(height - 1, -1, -1):
            for x in range(width - 1, -1, -1):
                if y == height - 1 and x == width - 1:
                    dp[y][x] = grid[y][x]
                    continue
                currW = grid[y][x]
                either = [dp[y][x]]
                if y < height - 1:
                    either.append(dp[y + 1][x] + currW)
                if x < width - 1:
                    either.append(dp[y][x + 1] + currW)
                dp[y][x] = min(either)

        return dp[0][0]


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1],
    ]
    print(sol.minPathSum(grid))
    print("Running Solution...")


"""
This solution took too much time

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        dp = [[float("inf")] * width for _ in range(height)]

        def dfs(y, x, pathWeight):
            currWeight = pathWeight + grid[y][x]
            dp[y][x] = min(currWeight, dp[y][x])
            if x > 0:
                dfs(y, x - 1, pathWeight + grid[y][x])
            if y > 0:
                dfs(y - 1, x, pathWeight + grid[y][x])

        dfs(height - 1, width - 1, 0)

        return dp[0][0]


"""
