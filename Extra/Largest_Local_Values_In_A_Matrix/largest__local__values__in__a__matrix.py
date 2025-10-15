from typing import Optional, List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def getVal(y, x):
            vList = [
                [grid[y + row][x + col] for col in range(-1, 2)] for row in range(-1, 2)
            ]
            tmp = []
            for row in vList:
                tmp += row
            return max(tmp)

        n = len(grid)
        m = n - 2
        newGrid = [[0] * m for _ in range(m)]
        for y in range(m):
            for x in range(m):
                newGrid[y][x] = getVal(y + 1, x + 1)
        return newGrid
        pass


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [9, 9, 8, 1],
        [5, 6, 2, 6],
        [8, 2, 6, 4],
        [6, 2, 2, 2],
    ]
    result = sol.largestLocal(grid)
    for row in result:
        print(row)
    print("Running Solution...")
