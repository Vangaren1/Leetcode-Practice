from typing import Optional, List
from collections import defaultdict
import pprint
import heapq

# Prim's algorithm solution


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        adj = defaultdict(list)
        visited = set()

        # build edges
        for index, point in enumerate(points):
            x, y = point
            for j in range(index + 1, n):
                nx, ny = points[j]
                dist = abs(x - nx) + abs(y - ny)
                adj[index].append((dist, j))
                adj[j].append((dist, index))

        totalCost = 0
        frontier = [[0, 0]]
        while len(visited) < n:

            cost, index = heapq.heappop(frontier)
            if index in visited:
                continue
            totalCost += cost
            visited.add(index)
            for neighborCost, neighbor in adj[index]:
                if neighbor not in visited:
                    heapq.heappush(frontier, (neighborCost, neighbor))

        return totalCost


if __name__ == "__main__":
    sol = Solution()
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(sol.minCostConnectPoints(points))
    print("Running Solution...")


"""
Kruskal Algorithm solution
        
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        edges = []

        for i in range(n):
            x, y = points[i]
            for j in range(i + 1, n):
                nx, ny = points[j]
                dist = abs(x - nx) + abs(y - ny)
                edges.append((dist, i, j))

        edges.sort()
        res = 0
        for dist, x, y in edges:
            if uf.union(x, y):
                res += dist

        return res


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

        """
