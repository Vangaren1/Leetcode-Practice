from typing import Optional, List

from collections import defaultdict, Counter, deque
import heapq




class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [ -c for c in count.values()]
        heapq.heapify(maxheap) 
        q = deque()
        time = 0
        while maxheap or q:
            time += 1
            if maxheap:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time
        
        

if __name__ == "__main__":
    tasks = ["A","A","A","B","B","B"]
    n =2
    
    s = Solution()
    print(s.leastInterval(tasks, n))
    print("Running Solution...")
