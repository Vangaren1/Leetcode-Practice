from typing import Optional, List
from collections import defaultdict


class CountSquares:

    def __init__(self):
        self.ptCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.ptCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptCount[(x, py)] * self.ptCount[(px, y)]
        return res


if __name__ == "__main__":
    sol = CountSquares()

    sol.add([1, 1])
    sol.add([2, 2])
    sol.add([1, 2])

    print(sol.count([2, 1]))
    print("Running Solution...")
