from typing import Optional, List


class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:

        for row in range(k // 2):
            for col in range(k):
                top = row + x
                bottom = (k - 1) + x - row
                grid[top][col + y], grid[bottom][col + y] = (
                    grid[bottom][col + y],
                    grid[top][col + y],
                )

        return grid


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [14, 3, 18, 16],
        [2, 14, 11, 20],
        [19, 19, 4, 15],
        [11, 15, 18, 6],
    ]
    x = 0
    y = 0
    k = 4

    print(sol.reverseSubmatrix(grid, x, y, k))
    print("Running Solution...")
