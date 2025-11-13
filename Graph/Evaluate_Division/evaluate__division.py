from typing import Optional, List
from collections import defaultdict
import heapq


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:

        adj = defaultdict(list)
        reachable = defaultdict(set)
        # build the adjacency list where adj[a] = [(b, a/b )]
        # reachable creates a list of all reachable nodes from a.  reachable[a] = [ b, c, d ]
        for index, equat in enumerate(equations):
            numerator = equat[0]
            denominator = equat[1]
            val1 = values[index]
            val2 = 1 / val1
            adj[numerator].append((denominator, val1))
            adj[denominator].append((numerator, val2))

        # determine reachability
        def dfs(start, node):
            for neighbor, _ in adj[node]:
                if neighbor not in reachable[start]:
                    reachable[start].add(neighbor)
                    dfs(start, neighbor)

        for node in adj.keys():
            dfs(node, node)

        def bfs(src, dest):
            if src == dest:
                return 0

            visited = set()
            queue = [(1, src)]

            while queue:
                curr, node = heapq.heappop(queue)
                if node == dest:
                    return curr

                visited.add(node)

                for neighbor, weight in adj[node]:
                    if neighbor not in visited:
                        heapq.heappush(queue, (curr * weight, neighbor))

            return 0

        results = []
        for q1, q2 in queries:
            # if either variable hasn't been seen, append -1
            if q1 not in adj or q2 not in adj:
                results.append(-1.0)
            # if it's not reachable, it can't be calculated
            elif q1 not in reachable[q2]:
                results.append(-1.0)
            # if it's the same value, it's always 1.0
            elif q1 == q2:
                results.append(1.0)
            else:
                results.append(bfs(q1, q2))

        return results


if __name__ == "__main__":
    sol = Solution()
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(sol.calcEquation(equations, values, queries))
    print("Running Solution...")
