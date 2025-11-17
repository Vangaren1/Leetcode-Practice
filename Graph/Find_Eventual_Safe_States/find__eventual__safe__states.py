from typing import Optional, List
from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n

        """
        unvisited = 0
        visited = 1
        safe = 2
        """

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True

            state[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            state[node] = 2
            return True

        results = []
        for index in range(len(graph)):
            if dfs(index):
                results.append(index)

        return results

        pass


if __name__ == "__main__":
    sol = Solution()
    graph = [[1, 3, 4, 5], [], [], [], [], [2, 4]]
    # Output: [2,4,5,6]

    print(sol.eventualSafeNodes(graph))
    print("Running Solution...")
