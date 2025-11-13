from typing import Optional, List
from collections import defaultdict, deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * len(graph)

        for index in range(n):

            if colors[index] != -1:
                continue

            colors[index] = 0
            queue = deque([index])

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if colors[neighbor] == -1:
                        colors[neighbor] = 1 - colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False

        return True


if __name__ == "__main__":
    sol = Solution()
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print(sol.isBipartite(graph))
    print("Running Solution...")
