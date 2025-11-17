from typing import Optional, List
from collections import defaultdict


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(set)
        n = len(graph)

        for index in range(len(graph)):
            for neighbor in graph[index]:
                adj[index].add(neighbor)

        results = []

        curr = [0]

        def dfs(i):
            # include i in the path
            if curr:
                tmp = curr[-1]
                if tmp == (n - 1):
                    results.append(curr.copy())
                    return

            for neighbors in adj[i]:
                curr.append(neighbors)
                dfs(neighbors)
                if curr:
                    curr.pop()

        dfs(0)
        return results

        pass


if __name__ == "__main__":
    sol = Solution()
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    # output [[0,1,3],[0,2,3]]

    print(sol.allPathsSourceTarget(graph))
    print("Running Solution...")
