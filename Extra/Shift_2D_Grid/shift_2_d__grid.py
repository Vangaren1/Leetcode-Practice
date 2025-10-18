from typing import Optional, List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        height = len(grid)
        width = len(grid[0])

        k = k % (height * width)

        # if k > width, shift the rows first
        if k >= width:
            rowShift = k // width
            for _ in range(rowShift):
                grid.insert(0, grid.pop())
            k -= rowShift * width

        for spaces in range(k):
            for row in range(height):
                nextRow = (row + 1) % height
                grid[nextRow].insert(0, grid[row].pop())
        return grid


if __name__ == "__main__":
    sol = Solution()
    grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    k = 4
    r = sol.shiftGrid(grid, k)
    for row in r:
        print(row)
    print("Running Solution...")
