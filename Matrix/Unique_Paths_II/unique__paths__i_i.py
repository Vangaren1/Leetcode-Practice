from typing import Optional, List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])

        dp = [[0] * width for _ in range(height)]

        def calulate(y, x):
            if obstacleGrid[y][x] == 1:
                return 0
            total = 0
            if y == height - 1 and x == width - 1:
                return 1
            if x < width - 1:
                total += dp[y][x + 1]
            if y < height - 1:
                total += dp[y + 1][x]
            return total

        for y in range(height - 1, -1, -1):
            for x in range(width - 1, -1, -1):
                dp[y][x] = calulate(y, x)

        return dp[0][0]

        pass


if __name__ == "__main__":
    sol = Solution()
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(sol.uniquePathsWithObstacles(obstacleGrid))
    print("Running Solution...")
