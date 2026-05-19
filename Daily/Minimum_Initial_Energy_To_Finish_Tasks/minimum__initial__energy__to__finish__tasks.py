from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1] - t[0], reverse=True)

        prev = 0
        total = 0
        for actual, minimum in tasks:
            total = max(total, prev + minimum)
            prev += actual

        return total


if __name__ == "__main__":
    sol = Solution()
    tasks = [[1, 1], [1, 3]]
    print(sol.minimumEffort(tasks))
    print("Running Solution...")
