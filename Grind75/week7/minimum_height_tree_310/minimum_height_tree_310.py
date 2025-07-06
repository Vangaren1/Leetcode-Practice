from typing import Optional, List
from collections import deque, defaultdict



class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        edgeCount = {}
        leaf = deque()
        for src, neighbor in adj.items():
            if len(neighbor) == 1:
                leaf.append(src)
            edgeCount[src] = len(neighbor)
            
        while leaf:
            if n <= 2:
                return list(leaf)
            for index in range(len(leaf)):
                node = leaf.popleft()
                n -= 1
                for nei in adj[node]:
                    edgeCount[nei] -= 1
                    if edgeCount[nei] == 1:
                        leaf.append(nei)
            
        
    
if __name__ == "__main__":
    n = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    
    s = Solution()

    print(s.findMinHeightTrees(n, edges))
    
    print("Running Solution...")
