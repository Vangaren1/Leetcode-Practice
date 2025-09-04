from typing import Optional, List

from common.graphnode import GraphNode as Node, print_graph_bfs, build_graph


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None
        cloneDict = {}

        def dfs(n: Optional["Node"]):
            if n is None:
                return None
            if n in cloneDict:
                return cloneDict[n]
            cloneDict[n] = Node(n.val)
            if n.neighbors:
                for neigh in n.neighbors:
                    cloneDict[n].neighbors.append(dfs(neigh))
            return cloneDict[n]

        return dfs(node)


if __name__ == "__main__":
    sol = Solution()
    adjList = [[2], [1, 3], [2]]
    node = build_graph(adjList)
    newNode = sol.cloneGraph(node)
    print("Running Solution...")
