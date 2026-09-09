from typing import Optional, List
import heapq
from collections import defaultdict



class UnionFind:
    def __init__(self, n):
        self.arr = [ i for i in range(n)]
        self.size [ 1 for i in range(n)]
        self.components = n
        
    def find(self, x):
        while self.arr[x] != x:
            x = self.arr[x]
        return x 
    
    def union(self, x, y)-> bool:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False 
        
        if self.size[rootX] < self.size[rootY]:
            rootX, rootY = rootY, rootX
        self.arr[rootY] = rootX
        self.size[rootX] += self.size[rootY]
        self.components -=1

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        
        logs.sort(key=lambda x: x[0])
        
        for date, a,b in logs:
            uf.union(a,b)
            if uf.components == 1:
                return date
            
        return -1 if uf.components > 1 else date        
    

if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
