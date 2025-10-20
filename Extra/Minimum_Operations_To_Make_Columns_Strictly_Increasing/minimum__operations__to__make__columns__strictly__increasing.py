from typing import Optional, List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        operations = 0

        for x in range(len(grid[0])):
            curr = grid[0][x]
            for y in range(1, len(grid)):
                tmp = grid[y][x]
                if tmp < curr + 1:
                    inc = (curr + 1) - tmp
                    operations += inc
                    curr = curr + 1
                else:
                    curr = tmp

        return operations


if __name__ == "__main__":
    sol = Solution()
    grid = [[3, 2], [1, 3], [3, 4], [0, 1]]

    print(sol.minimumOperations(grid))

    print("Running Solution...")
