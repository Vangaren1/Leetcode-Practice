from typing import Optional, List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        def sArea(y, x):
            val = grid[y][x]
            total = 2 if val > 0 else 0
            # from above
            if 0 < y < len(grid):
                if grid[y - 1][x] < val:
                    total += val - grid[y - 1][x]
            else:
                total += val
            # from below
            if 0 <= y < len(grid) - 1:
                if grid[y + 1][x] < val:
                    total += val - grid[y + 1][x]
            else:
                total += val
            # from the left
            if 0 < x < len(grid[0]):
                if grid[y][x - 1] < val:
                    total += val - grid[y][x - 1]
            else:
                total += val
            # from the right
            if 0 <= x < len(grid) - 1:
                if grid[y][x + 1] < val:
                    total += val - grid[y][x + 1]
            else:
                total += val
            return total

        res = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                res += sArea(y, x)
        return res


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 2], [3, 4]]
    print(sol.surfaceArea(grid))
    print("Running Solution...")
