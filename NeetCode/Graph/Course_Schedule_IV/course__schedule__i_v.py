from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        courses = [set() for _ in range(numCourses)]

        for courseA, courseB in prerequisites:
            courses[courseA].add(courseB)

        memo = {}

        def dfs(node, target):
            if (node, target) in memo:
                return memo[(node, target)]
            if node == target:
                memo[(node, target)] = True
                return True
            for neighbor in courses[node]:
                if dfs(neighbor, target):
                    memo[(node, target)] = True
                    return True
            memo[(node, target)] = False
            return False

        return [dfs(node, target) for node, target in queries]


if __name__ == "__main__":
    sol = Solution()
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2]]
    queries = [[0, 1], [3, 1]]
    print(sol.checkIfPrerequisite(numCourses, prerequisites, queries))
    print("Running Solution...")
