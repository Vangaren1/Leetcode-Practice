from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        results = []

        uf = self.UnionFind(n)

        for i in range(1, n):
            if nums[i] - nums[i - 1] < maxDiff:
                uf.union(i, i - 1)

        for src, dest in queries:
            results.append(uf.find(src) == uf.find(dest))

        return results

    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
            self.components = n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  # path compression
            return self.parent[x]

        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False

            # weighted union
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            self.components -= 1
            return True


if __name__ == "__main__":
    sol = Solution()
    n = 4
    nums = [2, 5, 6, 8]
    maxDiff = 2
    queries = [[0, 1], [0, 2], [1, 3], [2, 3]]
    print(sol.pathExistenceQueries(n, nums, maxDiff, queries))
    print("Running Solution...")
