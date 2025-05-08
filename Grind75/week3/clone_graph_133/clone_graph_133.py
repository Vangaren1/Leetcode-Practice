from typing import Optional, List

from common.graphnode import GraphNode as Node, print_graph_bfs, build_graph

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}

        def bfs(n: Optional['Node']):
            nonlocal seen
            if n in seen:
                return n
            seen[n] = Node(n.val)
            for neigh in n.neighbors:
                if neigh in seen:
                    seen[n].neighbors.append(seen[neigh])
                else:
                    bfs(neigh)
                    seen[n].neighbors.append(seen[neigh])
                
        bfs(node)
        return seen[node]
        


if __name__ == "__main__":
    print("Running Solution...")
