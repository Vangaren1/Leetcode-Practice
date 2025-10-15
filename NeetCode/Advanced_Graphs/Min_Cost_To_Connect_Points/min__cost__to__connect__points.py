from typing import Optional, List
from collections import defaultdict
import pprint


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        edges = []
        for index in range(len(points)):
            y, x = points[index]
            for ptr in range(len(points)):
                dy, dx = points[ptr]
                if y != dy and x != dx:
                    weight = abs(y - dy) + abs(x - dx)
                    edges.append((weight, index, ptr))

        edges.sort(key=lambda x: x[0])

        uf = UnionFind(len(points))

        mst_weight = 0

        for weight, s, d in edges:
            if uf.union(s, d):
                mst_weight += weight
        return mst_weight


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False

        # attach smaller rank tree under larger one
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True


if __name__ == "__main__":
    sol = Solution()
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(sol.minCostConnectPoints(points))
    print("Running Solution...")
