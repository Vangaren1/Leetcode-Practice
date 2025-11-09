from typing import Optional, List
from collections import defaultdict
import heapq


class Solution:
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n + 1))  # 1..n
            self.size = [1] * (n + 1)

        def find(self, x):
            while x != self.parent[x]:
                self.parent[x] = self.parent[self.parent[x]]  # path compression
                x = self.parent[x]
            return x

        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]

    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        dsu = self.DSU(c)
        for u, v in connections:
            dsu.union(u, v)

        # group nodes by component
        groups = defaultdict(list)
        for i in range(1, c + 1):
            groups[dsu.find(i)].append(i)
        # min-heap per component
        for r in groups:
            heapq.heapify(groups[r])

        closed = [False] * (c + 1)
        ans = []

        for typ, x in queries:
            if typ == 1:
                if not closed[x]:
                    ans.append(x)
                else:
                    r = dsu.find(x)
                    h = groups[r]
                    while h and closed[h[0]]:
                        heapq.heappop(h)  # lazy delete closed nodes
                    ans.append(h[0] if h else -1)
            else:  # typ == 2
                closed[x] = True

        return ans


if __name__ == "__main__":
    sol = Solution()
    c = 5
    connections = [[1, 2], [2, 3], [3, 4], [4, 5]]
    queries = [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]
    print(sol.processQueries(c, connections, queries))

    c = 3
    connections = []
    queries = [[1, 1], [2, 1], [1, 1]]
    print(sol.processQueries(c, connections, queries))

    c = 2
    connections = [[1, 2]]
    queries = [
        [1, 2],
        [2, 1],
        [1, 2],
        [1, 1],
        [2, 2],
        [1, 2],
        [2, 2],
        [1, 1],
        [1, 1],
        [2, 1],
        [1, 2],
        [1, 2],
        [1, 1],
        [2, 1],
        [1, 1],
        [1, 1],
        [1, 1],
        [2, 1],
        [2, 1],
        [2, 1],
        [1, 2],
        [2, 1],
        [2, 2],
        [1, 2],
        [1, 1],
        [2, 2],
        [2, 1],
        [2, 2],
    ]
    print(sol.processQueries(c, connections, queries))
    print("Running Solution...")


"""
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

    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        qu = self.WeightedQuickUnion(c + 1)
        connections.sort()
        for left, right in connections:
            qu.union(left, right)

        onOrOff = [True] * (c + 1)

        results = []

        for action, station in queries:
            if action == 1:
                # if the station is active, return that value
                if onOrOff[station]:
                    results.append(station)
                else:
                    # otherwise find the next one that is active
                    root = qu.root(station)
                    ptr = root
                    while ptr <= c and onOrOff[ptr] == False:
                        ptr += 1
                        while ptr < c and qu.root(ptr) != root:
                            ptr += 1
                    if ptr < c:
                        results.append(ptr)
                    else:
                        results.append(-1)
            if action == 2:
                onOrOff[station] = False

        return results    
    """
