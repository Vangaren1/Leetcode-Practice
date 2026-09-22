from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ndegree = [0 for _ in range(n)]

        for src, dst in edges:
            ndegree[dst] += 1

        if ndegree.count(0) > 1:
            return -1

        return ndegree.index(0)


if __name__ == "__main__":
    sol = Solution()
    n = 3
    edges = [[0, 1], [1, 2]]
    print(sol.findChampion(n, edges))
    print("Running Solution...")
