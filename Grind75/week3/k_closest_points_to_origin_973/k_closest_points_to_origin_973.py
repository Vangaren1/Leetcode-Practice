from typing import Optional, List

import heapq

class Solution:
    
    class Coord:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.dist = x**2 + y**2
            
        def __lt__(self, other):
            return self.dist < other.dist
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hList = []
        
        for p in points: 
            hList.append(self.Coord(p[0], p[1]))
        
        heapq.heapify(hList)
            
        results = []
        
        for i in range(k):
            tmp = heapq.heappop(hList)
            results.append([tmp.x, tmp.y])
            
        
        return results

if __name__ == "__main__":
    
    s = Solution()
    
    points = [[-5,4],[-6,-5],[4,6]]
    k = 2
    
    s.kClosest(points, k)
    
    
    print("Running Solution...")
