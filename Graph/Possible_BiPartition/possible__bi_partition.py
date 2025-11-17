from typing import Optional, List
from collections import defaultdict, deque


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(set)

        for a, b in dislikes:
            adj[a].add(b)
            adj[b].add(a)

        colors = [-1] * n

        for index in range(1, n + 1):

            if colors[index - 1] != -1:
                continue

            colors[index - 1] = 0
            queue = deque([index])

            while queue:
                node = queue.popleft()

                for neighbor in adj[node]:
                    if colors[neighbor - 1] == -1:
                        colors[neighbor - 1] = 1 - colors[node - 1]
                        queue.append(neighbor)
                    elif colors[neighbor - 1] == colors[node - 1]:
                        return False
        return True


if __name__ == "__main__":
    sol = Solution()

    n = 3
    dislikes = [[1, 2], [1, 3], [2, 3]]
    print(sol.possibleBipartition(n, dislikes))
    print("Running Solution...")
