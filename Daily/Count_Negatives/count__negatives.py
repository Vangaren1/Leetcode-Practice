from typing import Optional, List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        count = 0
        for g in grid:

            for ptr in range(width - 1, -1, -1):
                if g[ptr] < 0:
                    count += 1
                else:
                    break
        return count


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3],
    ]
    print(sol.countNegatives(grid))
    print("Running Solution...")
