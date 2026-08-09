from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        taskList = []
        for index, (start_time, duration) in enumerate(tasks):
            taskList.append((start_time, duration, index))

        taskList.sort()

        n = len(tasks)
        time = 0
        index = 0

        available = []
        results = []

        while index < n or available:

            if not available and time < taskList[index][0]:
                time = taskList[index][0]

            while index < n and taskList[index][0] <= time:

                _, ptime, org_index = taskList[index]
                heapq.heappush(available, (ptime, org_index))
                index += 1

            ptime, org_index = heapq.heappop(available)

            results.append(org_index)
            time += ptime

        return results


if __name__ == "__main__":
    sol = Solution()
    tasks = [[5, 2], [4, 4], [4, 1], [2, 1], [3, 3]]
    print(sol.getOrder(tasks))
    print("Running Solution...")
