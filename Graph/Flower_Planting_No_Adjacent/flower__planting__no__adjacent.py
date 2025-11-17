from typing import Optional, List
from collections import defaultdict, deque


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = defaultdict(set)

        for a, b in paths:
            adj[a].add(b)
            adj[b].add(a)

        color = [0] * (n + 1)

        for garden in range(1, n + 1):

            used = {color[neighbor] for neighbor in adj[garden]}

            for c in range(1, 5):
                if c not in used:
                    color[garden] = c
                    break
        return color[1:]


if __name__ == "__main__":
    sol = Solution()
    n = 7
    paths = [[2, 4], [7, 1], [3, 2], [6, 1], [7, 2], [3, 6], [4, 1], [3, 7], [4, 5]]
    print(sol.gardenNoAdj(n, paths))
    print("Running Solution...")
