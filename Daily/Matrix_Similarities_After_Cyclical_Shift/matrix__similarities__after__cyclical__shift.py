from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        if n <= 1:
            return True

        k = k % n

        for row in mat:
            if len(set(row)) > 1:
                for i in range(n):
                    if row[i] != row[(k + i) % n]:
                        return False
        return True


if __name__ == "__main__":
    sol = Solution()

    mat = [[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]]
    k = 2
    print(sol.areSimilar(mat, k))

    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 4
    print(sol.areSimilar(mat, k))

    print("Running Solution...")
