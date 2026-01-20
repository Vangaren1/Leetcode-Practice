from typing import Optional, List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negCount = 0
        total = 0
        minNum = float("inf")
        for row in matrix:
            for num in row:
                if num < 0:
                    negCount += 1
                total += abs(num)
                minNum = min(minNum, abs(num))

        if negCount % 2 == 1:
            total -= minNum * 2
        return total

        pass


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
    print(sol.maxMatrixSum(matrix))
    print("Running Solution...")
