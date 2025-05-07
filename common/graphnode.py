# Definition for a Node.
class GraphNode:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
from collections import deque

def print_graph_bfs(start: 'GraphNode'):
    visited = set()
    queue = deque([start])
    print("Graph structure:")

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        neighbors_vals = [n.val for n in node.neighbors]
        print(f"Node {node.val}: Neighbors -> {neighbors_vals}")
        for neighbor in node.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)

def build_graph(adjList: list[list[int]]) -> 'GraphNode':
    if not adjList:
        return None

    # Step 1: Create all nodes
    nodes = {}
    for i in range(len(adjList)):
        nodes[i + 1] = GraphNode(i + 1)

    # Step 2: Assign neighbors
    for i, neighbors in enumerate(adjList):
        node = nodes[i + 1]
        node.neighbors = [nodes[n] for n in neighbors]

    # Return the node with val = 1 (i.e., index 0), which is the root
    return nodes[1]
