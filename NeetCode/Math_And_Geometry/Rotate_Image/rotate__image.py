from typing import Optional, List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for index in range(n // 2):
            matrix[index], matrix[-(index + 1)] = matrix[-(index + 1)], matrix[index]

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix)
    for m in matrix:
        print(m)
    print("Running Solution...")
