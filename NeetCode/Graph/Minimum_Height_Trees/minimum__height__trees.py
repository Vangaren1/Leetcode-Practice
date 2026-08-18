from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = [[] for _ in range(n)]
        for source, destination in edges:
            adj[source].append(destination)
            adj[destination].append(source)

        degree = [(len(adj[i])) for i in range(n)]
        leaves = [index for index in range(n) if degree[index] == 1]
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            newLeaves = []

            for leaf in leaves:
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        newLeaves.append(neighbor)
            leaves = newLeaves

        return leaves


if __name__ == "__main__":
    sol = Solution()
    n = 5
    edges = [[0, 1], [3, 1], [2, 3], [4, 1]]
    print(sol.findMinHeightTrees(n, edges))

    print("Running Solution...")


""" 

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]

        for source, destination in edges:
            adj[source].append(destination)
            adj[destination].append(source)

        def dfs(node, parent):
            max_depth = 0

            for neighbor in adj[node]:
                if neighbor != parent:
                    max_depth = max(max_depth, 1 + dfs(neighbor, node))

            return max_depth

        heights = []
        for index in range(n):
            heights.append(dfs(index, None))

        minimumHeight = min(heights)
        return [index for index in range(n) if heights[index] == minimumHeight]

        
"""
