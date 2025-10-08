from typing import Optional, List
import heapq


class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        res = []

        def dist(y, x):
            return abs((y - rCenter)) + abs((x - cCenter))

        for y in range(rows):
            for x in range(cols):
                res.append((dist(y, x), [y, x]))

        res.sort(key=lambda x: x[0])
        return [i[1] for i in res]

        pass


if __name__ == "__main__":
    sol = Solution()
    rows = 1
    cols = 2
    rCenter = 0
    cCenter = 0
    print(sol.allCellsDistOrder(rows, cols, rCenter, cCenter))
    print("Running Solution...")
