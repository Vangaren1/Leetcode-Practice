from typing import Optional, List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            courses[a].append(b)

        checking = set()
        seen = set()

        def dfs(course):
            if course in checking:
                return False
            if course in seen:
                return True
            checking.add(course)

            for pre in courses[course]:
                check = dfs(pre)
                if not check:
                    return False

            checking.remove(course)
            seen.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
            else:
                courses[c] = []
        return True


if __name__ == "__main__":
    sol = Solution()
    numCourses = 5
    prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
    sol.canFinish(numCourses, prerequisites)
    print("Running Solution...")
