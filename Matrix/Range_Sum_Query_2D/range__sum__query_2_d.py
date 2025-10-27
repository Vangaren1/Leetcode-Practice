from typing import Optional, List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = [row.copy() for row in matrix]
        self.height = len(matrix)
        self.width = len(matrix[0])

        self.dp = [[0] * (self.width + 1) for _ in range(self.height + 1)]

        for y in range(1, self.height + 1):
            for x in range(1, self.width + 1):
                self.dp[y][x] = (
                    matrix[y - 1][x - 1]
                    + self.dp[y - 1][x]
                    + self.dp[y][x - 1]
                    - self.dp[y - 1][x - 1]
                )

        pass

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row1][col2 + 1]
            - self.dp[row2 + 1][col1]
            + self.dp[row1][col1]
        )


if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
    sol = NumMatrix(matrix)
    print(sol.sumRegion(0, 0, 2, 2))
    print("Running Solution...")
