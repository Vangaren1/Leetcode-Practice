from typing import Optional, List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        newMatrix = [[0] * n for _ in range(m)]

        for y in range(m):
            for x in range(n):
                if matrix[y][x] == -1:
                    newMatrix[y][x] = max([matrix[i][x] for i in range(m)])
                else:
                    newMatrix[y][x] = matrix[y][x]
        return newMatrix
        pass


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, -1], [4, -1, 6], [7, 8, 9]]
    result = sol.modifiedMatrix(matrix)
    for row in result:
        print(row)
    print("Running Solution...")
