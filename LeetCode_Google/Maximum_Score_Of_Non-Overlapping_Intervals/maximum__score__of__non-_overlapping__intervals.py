from typing import Optional, List
import heapq
from collections import defaultdict
from bisect import bisect_left


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sortedIntervals = [(inter, index) for index, inter in enumerate(intervals)]

        sortedIntervals.sort()

        interDictionary = defaultdict(list)
        startingPoints = []
        for inter in sortedIntervals:
            startAt = inter[0][0]
            if len(startingPoints) == 0 or startingPoints[-1] < startAt:
                startingPoints.append(startAt)
            interDictionary[startAt].append(inter)

        # return the max value and next interval end, and path taken
        def dfs(start, path):
            if n == 0 or (n > 0 and start >= startingPoints[-1]):
                return (0, float("inf"), path)
            index = bisect_left(startingPoints, start)

            best = float("-inf")
            bestIndex = None
            while index < len(startingPoints):
                point = startingPoints[index]

                for interval in interDictionary[point]:
                    endIdx = interval[0][1]
                    score = interval[0][2]
                    newPath = path.copy()
                    newPath.append(interval[1])
                    test = dfs(endIdx + 1, newPath)
                    if test[0] + score > best:
                        best = test[0] + score
                        bestIndex = test[1]
                        path = newPath
                index += 1

            return (best, bestIndex, path)

        for interval in sortedIntervals:
            print(dfs(interval[0][0], []))


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
