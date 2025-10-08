from typing import Optional, List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        height = len(matrix)
        width = len(matrix[0])

        newMatrix = [[0] * height for _ in range(width)]

        for x in range(width):
            for y in range(height):
                newMatrix[x][y] = matrix[y][x]

        return newMatrix
        pass


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result = sol.transpose(matrix)
    for row in result:
        print(row)
    print("Running Solution...")
