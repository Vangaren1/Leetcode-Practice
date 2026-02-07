from typing import Optional, List
import heapq
from collections import defaultdict, Counter


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        c = defaultdict(int)
        mVal = -1
        vals = []
        first = {}
        last = {}

        for index, num in enumerate(nums):
            c[num] += 1

            if c[num] > mVal:
                mVal = c[num]
                vals = [num]
            elif c[num] == mVal:
                vals.append(num)

            if num not in first:
                first[num] = index
            last[num] = index

        smallest = float("inf")
        for v in vals:
            tmp = last[v] - first[v] + 1
            smallest = min(smallest, tmp)
        return smallest


if __name__ == "__main__":
    sol = Solution()

    assert sol.findShortestSubArray([1, 2, 2, 3, 1]) == 2
    assert sol.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]) == 6
    print("Running Solution...")
