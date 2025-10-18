from typing import Optional, List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        n = len(mat)
        for y in range(n):
            total += mat[y][y]
            total += mat[y][n - y - 1]
        if n % 2 == 1:
            mid = n // 2
            total -= mat[mid][mid]
        return total


if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.diagonalSum(mat))
    print("Running Solution...")
