from typing import Optional, List
from collections import defaultdict


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervalMap = defaultdict(int)

        for start, end in intervals:
            currLen = end - start + 1
            for i in range(start, end + 1):
                if i in intervalMap:
                    intervalMap[i] = min(currLen, intervalMap[i])
                else:
                    intervalMap[i] = currLen

        res = []
        for q in queries:
            if q in intervalMap:
                res.append(intervalMap[q])
            else:
                res.append(-1)
        return res

        pass


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 3], [2, 3], [3, 7], [6, 6]]
    queries = [2, 3, 1, 7, 6, 8]

    print(sol.minInterval(intervals, queries))

    Output = [2, 2, 3, 5, 1, -1]

    print("Running Solution...")
