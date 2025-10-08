from typing import Optional, List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        total = 0

        maxColVal = [0] * len(grid[0])
        # get the top value
        for y in range(len(grid)):
            maxRowVal = 0
            for x in range(len(grid[0])):
                # get the xy value
                if grid[y][x] > 0:
                    total += 1
                    maxRowVal = max(maxRowVal, grid[y][x])
                    maxColVal[x] = max(maxColVal[x], grid[y][x])
            # add the xz value
            total += maxRowVal

        # add the yz values
        for colVal in maxColVal:
            total += colVal

        return total


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 2], [3, 4]]
    print(sol.projectionArea(grid))
    print("Running Solution...")
