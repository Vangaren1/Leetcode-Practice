from typing import Optional, List
from collections import deque

class Solution:
    class Union:
        def __init__(self, size):
            self.id = list(range(size))
            self.size = [1] * size
        def root(self, i):
            while i != self.id[i]:
                self.id[i] = self.id[self.id[i]] 
                i = self.id[i]
            return i
        def connected(self, p, q):
            return self.root(p) == self.root(q)
        def union(self, p, q):
            i = self.root(p)
            j = self.root(q)
            if i != j:
                if self.size[i] < self.size[j]:
                    self.id[i] = j
                    self.size[j] += self.size[i]
                else:
                    self.id[j] = i
                    self.size[i] += self.size[j]
            
            
            
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        for index in range(len(edges)):
            edgeSet = deque(edges)
            edgeSet.rotate(index)
            un = self.Union(n)
            print('new order')
            for left, right in list(edgeSet):
                print("{} {}".format(left, right))
                un.union(left, right)
            print(list(set(un.id)))
        return list(set(un.id))
        

if __name__ == "__main__":
    n = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    
    s = Solution()
    u = s.Union(n)

    print(s.findMinHeightTrees(n, edges))
    
    print("Running Solution...")
