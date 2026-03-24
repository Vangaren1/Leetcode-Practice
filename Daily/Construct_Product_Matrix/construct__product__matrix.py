from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        height = len(grid)
        width = len(grid[0])
        n = height * width

        prefix = [[1 for _ in range(width)] for _ in range(height)]
        suffix = [[1 for _ in range(width)] for _ in range(height)]
        result = [[1 for _ in range(width)] for _ in range(height)]

        for j in range(n - 2, -1, -1):
            sy = (j + 1) // width
            sx = (j + 1) % width
            ny = (j) // width
            nx = (j) % width
            suffix[ny][nx] = suffix[sy][sx] * grid[sy][sx]

        result[0][0] = suffix[0][0]
        for i in range(1, n):
            py = (i - 1) // width
            px = (i - 1) % width
            prefix[i // width][i % width] = prefix[py][px] * grid[py][px]
            result[py][px] = (prefix[py][px] * suffix[py][px]) % 12345

        ly = (n - 1) // width
        lx = (n - 1) % width
        result[ly][lx] = prefix[ly][lx]

        return result


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [1, 2],
        [3, 4],
    ]
    print(sol.constructProductMatrix(grid))
    print("Running Solution...")
