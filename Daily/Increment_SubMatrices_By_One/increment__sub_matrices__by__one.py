from typing import Optional, List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]

        for startY, startX, endY, endX in queries:

            for y in range(startY, endY + 1):
                for x in range(startX, endX + 1):
                    mat[y][x] += 1

        return mat


# times out on large numbers, need to redo with prefix sum


if __name__ == "__main__":
    sol = Solution()
    n = 3
    queries = [[1, 1, 2, 2], [0, 0, 1, 1]]
    r = sol.rangeAddQueries(n, queries)
    for row in r:
        print(row)
    print("Running Solution...")
