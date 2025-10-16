from typing import Optional, List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [
            max([len(str(grid[i][j])) for i in range(len(grid))])
            for j in range(len(grid[0]))
        ]


if __name__ == "__main__":
    sol = Solution()
    grid = [[1], [22], [333]]
    print(sol.findColumnWidth(grid))
    print("Running Solution...")
