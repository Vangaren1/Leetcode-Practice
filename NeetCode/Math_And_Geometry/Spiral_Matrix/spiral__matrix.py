from typing import Optional, List
from functools import partial


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        results = []
        height = len(matrix)
        width = len(matrix[0])
        remaining = height * width
        direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dirPos = 0
        seen = set()
        y, x = 0, 0

        while remaining > 0:
            seen.add((y, x))
            results.append(matrix[y][x])
            remaining -= 1

            dy, dx = direction[dirPos]

            y, x = y + dy, x + dx

            if (y, x) in seen or y == height or y < 0 or x < 0 or x == width:
                y, x = y - dy, x - dx
                dirPos = (dirPos + 1) % 4
                dy, dx = direction[dirPos]
                y, x = y + dy, x + dx
        return results


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    print(sol.spiralOrder(matrix))
    print("Running Solution...")
