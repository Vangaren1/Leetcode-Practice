from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        dist = [float("inf") for i in range(n)]
        # store tuples, where origin:(dest, weight)
        adj = defaultdict(list)
        visited = set()

        for s, d, w in edges:
            adj[s].append((d, w))
            adj[d].append((s, 2 * w))

        queue = [(0, 0)]

        while queue:
            weight, curr = heapq.heappop(queue)
            if curr in visited:
                continue
            visited.add(curr)
            dist[curr] = min(weight, dist[curr])

            for dest, w in adj[curr]:
                if dest not in visited:
                    heapq.heappush(queue, (weight + w, dest))

        return dist[-1] if dist[-1] != float("inf") else -1


if __name__ == "__main__":
    sol = Solution()
    edges = [
        [1, 2, 17],
        [1, 0, 6],
        [1, 3, 5],
        [2, 4, 12],
        [1, 4, 19],
        [4, 3, 11],
        [2, 3, 4],
        [0, 2, 20],
        [0, 3, 3],
        [3, 0, 25],
    ]
    print(sol.minCost(5, edges))
    print("Running Solution...")
