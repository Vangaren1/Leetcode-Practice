from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        zero, ninety, one80, two70 = True, True, True, True

        for y in range(n):
            for x in range(n):
                if mat[y][x] != target[y][x]:
                    zero = False
                if mat[y][x] != target[x][n - y - 1]:
                    ninety = False
                if mat[y][x] != target[n - 1 - y][n - 1 - x]:
                    one80 = False
                if mat[y][x] != target[n - 1 - x][y]:
                    two70 = False
        return ninety or one80 or two70 or zero


if __name__ == "__main__":
    sol = Solution()
    mat = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]
    target = [
        [1, 1, 1],
        [0, 1, 0],
        [0, 0, 0],
    ]
    print(sol.findRotation(mat, target))

    mat = [[0, 1], [1, 1]]
    target = [[1, 0], [0, 1]]
    print(sol.findRotation(mat, target))

    mat = [[0, 1], [1, 0]]
    target = [[1, 0], [0, 1]]
    print(sol.findRotation(mat, target))
    print("Running Solution...")
