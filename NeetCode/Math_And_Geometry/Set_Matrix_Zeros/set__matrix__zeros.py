from typing import Optional, List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        height = len(matrix)
        width = len(matrix[0])

        rows = set()
        cols = set()
        for y in range(height):
            for x in range(width):
                if matrix[y][x] == 0:
                    rows.add(y)
                    cols.add(x)

        for row in rows:
            matrix[row] = [0] * width

        for y in range(height):
            for col in cols:
                matrix[y][col] = 0


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    sol.setZeroes(matrix)
    for m in matrix:
        print(m)
    print("Running Solution...")
