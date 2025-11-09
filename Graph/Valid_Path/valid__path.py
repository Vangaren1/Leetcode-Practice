from typing import Optional, List
from collections import defaultdict


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:

        visited = set()

        adj = defaultdict(list)
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for dest in adj[node]:
                if dest not in visited and dfs(dest):
                    return True
            return False

        return dfs(source)


if __name__ == "__main__":
    sol = Solution()
    n = 10
    edges = [
        [0, 7],
        [0, 8],
        [6, 1],
        [2, 0],
        [0, 4],
        [5, 8],
        [4, 7],
        [1, 3],
        [3, 5],
        [6, 5],
    ]
    source = 7
    destination = 5
    print(sol.validPath(n, edges, source, destination))
    print("Running Solution...")
