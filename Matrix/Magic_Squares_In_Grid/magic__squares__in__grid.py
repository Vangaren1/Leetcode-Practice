from typing import Optional, List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        if height < 3 or width < 3:
            return 0

        def square(y, x):
            oneThru9 = set(range(1, 10))

            rows = []
            cols = [[], [], []]
            for ny in range(y, y + 3):
                rows.append(sum(grid[y][x : x + 3]))

                for nx in range(x, x + 3):
                    tmp = grid[ny][nx]
                    cols[nx - x].append(tmp)
                    if tmp not in oneThru9:
                        return 0
                    oneThru9.remove(tmp)
            cols = [sum(c) for c in cols]
            print(all(cols))
            leftToRight = grid[y][x] + grid[y + 1][x + 1] + grid[y + 2][x + 2]
            rightToLeft = grid[y][x + 2] + grid[y + 1][x + 1] + grid[y + 2][x]
            if leftToRight != rightToLeft:
                return 0
            if (
                len(set(rows)) == 1
                and len(set(cols)) == 1
                and rows[0] == cols[0] == leftToRight == rightToLeft
            ):
                return 1
            return 0

        total = 0

        for y in range(height - 2):
            for x in range(width - 2):
                total += square(y, x)
        return total


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [4, 3, 8, 4],
        [9, 5, 7, 9],
        [2, 1, 6, 2],
    ]
    print(sol.numMagicSquaresInside(grid))
    print("Running Solution...")
