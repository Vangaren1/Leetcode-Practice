from typing import Optional, List
import heapq


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        results = []

        for index, row in enumerate(mat):
            results.append((sum(row), index))

        results.sort(key=lambda x: (x[0], x[1]))

        return [i[1] for i in results[:k]]

        pass


if __name__ == "__main__":
    sol = Solution()
    mat = [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ]
    k = 3
    print(sol.kWeakestRows(mat, k))
    print("Running Solution...")
