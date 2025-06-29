from typing import Optional, List

from collections import defaultdict


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskDict = defaultdict(int)
        for t in tasks:
            taskDict[t] += 1
        waitQueue = defaultdict(lambda: n)
        
        
        
        count = 0
        while taskDict.keys():
            
            count += 1
            
            curr = None
            potential = [ (key, val) for key, val in taskDict.items() if key not in waitQueue.keys()]
            potential.sort(key= lambda x: x[1], reverse=True)
            if potential:
                curr = potential[0][0]
                taskDict[curr] -= 1
                if taskDict[curr] == 0:
                    taskDict.pop(curr)
            
            if curr:
                waitQueue[curr] = n+1
            
            #reduce the countdown for each item in the wait Queue
            #remove if countdown is 0
            keyQueue = list(waitQueue.keys())
            for key in keyQueue:
                waitQueue[key] -= 1
                if waitQueue[key] == 0:
                    waitQueue.pop(key)
                
        return count

if __name__ == "__main__":
    tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
    n =2
    
    s = Solution()
    print(s.leastInterval(tasks, n))
    print("Running Solution...")
