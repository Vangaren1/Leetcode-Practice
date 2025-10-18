from typing import Optional, List
import math


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.mVal = self.n**2 - 1

    def find(self, value):
        x = -1
        for row in range(self.n):
            x = self.grid[row].count(value)
            if x != 0:
                return (row, self.grid[row].index(value))

    def adjacentSum(self, value: int) -> int:
        y, x = self.find(value)
        total = 0
        if y < self.n - 1:
            total += self.grid[y + 1][x]
        if y > 0:
            total += self.grid[y - 1][x]
        if x < self.n - 1:
            total += self.grid[y][x + 1]
        if x > 0:
            total += self.grid[y][x - 1]
        return total

    def diagonalSum(self, value: int) -> int:
        y, x = self.find(value)
        total = 0
        if y < self.n - 1 and x < self.n - 1:
            total += self.grid[y + 1][x + 1]
        if y < self.n - 1 and x > 0:
            total += self.grid[y + 1][x - 1]
        if y > 0 and x < self.n - 1:
            total += self.grid[y - 1][x + 1]
        if y > 0 and x > 0:
            total += self.grid[y - 1][x - 1]
        return total


if __name__ == "__main__":
    grid = [
        [1, 2, 0, 3],
        [4, 7, 15, 6],
        [8, 9, 10, 11],
        [12, 13, 14, 5],
    ]
    sol = NeighborSum(grid)

    print(sol.adjacentSum(1))
    print(sol.adjacentSum(4))

    print("Running Solution...")
