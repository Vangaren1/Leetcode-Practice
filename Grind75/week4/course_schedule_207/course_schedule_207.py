from typing import Optional, List

from common.graphnode import GraphNode as Node, print_graph_bfs, build_graph

class Solution:    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courseList = [ [] for _ in range(numCourses) ]
        
        for req in prerequisites:
            courseList[req[0]].append(req[1])
            
        seen = set()

        def dfs(course):
            nonlocal seen
            if course in seen:
                return True
            seen.add(course)
            for req in courseList[course]:
                check = dfs(req)
                if check:
                    return True 
            seen.remove(course)
            return False
            
        for i in range(numCourses):
            check = dfs(i)
            if check:
                return False
        
        return True


if __name__ == "__main__":
    s = Solution()
    
    numCourses = 5
    prerequisites = [[1,4],[2,4],[3,1],[3,2]]
    assert s.canFinish(numCourses, prerequisites) == True
    
    print("Running Solution...")
