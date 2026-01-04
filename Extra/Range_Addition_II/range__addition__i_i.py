from typing import Optional, List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minX, minY = m, n

        for x, y in ops:
            minX = min(minX, x)
            minY = min(minY, y)

        return minX * minY


if __name__ == "__main__":
    sol = Solution()

    m = 3
    n = 3
    ops = [[2, 2], [3, 3]]
    print(sol.maxCount(m, n, ops))

    ops = [
        [2, 2],
        [3, 3],
        [3, 3],
        [3, 3],
        [2, 2],
        [3, 3],
        [3, 3],
        [3, 3],
        [2, 2],
        [3, 3],
        [3, 3],
        [3, 3],
    ]
    print(sol.maxCount(m, n, ops))

    print(sol.maxCount(m, n, []))
    print("Running Solution...")
