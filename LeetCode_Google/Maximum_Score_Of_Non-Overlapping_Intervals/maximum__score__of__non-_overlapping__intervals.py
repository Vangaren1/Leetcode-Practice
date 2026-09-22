from typing import Optional, List
import heapq
from collections import defaultdict
from bisect import bisect_left


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sortedIntervals = [(inter, index) for index, inter in enumerate(intervals)]

        sortedIntervals.sort()

        memo = {}

        def dfs(index, remaining):
            if index >= n or remaining == 0:
                return (0, [])

            if (index, remaining) in memo:
                return memo[(index, remaining)]

            # option 1: don't take this interval
            skip = dfs(index + 1, remaining)


if __name__ == "__main__":
    sol = Solution()
    intervals = [
        [1, 3, 2],
        [4, 5, 2],
        [1, 5, 5],
        [6, 9, 3],
        [6, 7, 1],
        [8, 9, 1],
    ]
    print(sol.maximumWeight(intervals))
    print("Running Solution...")
