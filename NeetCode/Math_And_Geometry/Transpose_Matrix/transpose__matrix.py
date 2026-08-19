from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        height = len(matrix)
        width = len(matrix[0])

        newMatrix = [[0 for _ in range(height)] for _ in range(width)]

        for y in range(height):
            for x in range(width):
                newMatrix[x][y] = matrix[y][x]
        return newMatrix
        pass


if __name__ == "__main__":
    sol = Solution()
    Input = [
        [1, 0, 5],
        [2, 4, 3],
    ]
    print(sol.transpose(Input))
    print("Running Solution...")
