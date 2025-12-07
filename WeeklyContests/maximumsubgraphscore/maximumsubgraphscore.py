from typing import Optional, List


class Solution:
    class WeightedQuickUnion:
        def __init__(self, n):
            self.parent = [i for i in range(n)]
            self.size = [1] * n

        def root(self, i):
            while i != self.parent[i]:
                self.parent[i] = self.parent[self.parent[i]]  # path compression
                i = self.parent[i]
            return i

        def connected(self, a, b):
            return self.root(a) == self.root(b)

        def union(self, a, b):
            rootA = self.root(a)
            rootB = self.root(b)
            if rootA == rootB:
                return
            # attach smaller tree under larger tree
            if self.size[rootA] < self.size[rootB]:
                self.parent[rootA] = rootB
                self.size[rootB] += self.size[rootA]
            else:
                self.parent[rootB] = rootA
                self.size[rootA] += self.size[rootB]

    def maxSubgraphScore(
        self, n: int, edges: List[List[int]], good: List[int]
    ) -> List[int]:

        qu = self.WeightedQuickUnion(n)
        for edge in edges:
            qu.union(edge[0], edge[1])

        print(qu.parent)
        pass


if __name__ == "__main__":
    sol = Solution()
    n = 3
    edges = [[0, 1], [1, 2]]
    good = [1, 0, 1]

    print(sol.maxSubgraphScore(n, edges, good))
    print("Running Solution...")
