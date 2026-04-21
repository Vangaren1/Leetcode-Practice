from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(n):
            s = str(n)[::-1]
            return int(s)

        rDict = {}

        minFound = float("inf")
        for j, num in enumerate(nums):
            rnum = reverse(num)
            if num in rDict:
                i = rDict[num]
                if i < j:
                    minFound = min(minFound, abs(i - j))
            rDict[rnum] = j
        return minFound if minFound < float("inf") else -1


if __name__ == "__main__":
    sol = Solution()
    nums = [21, 120]
    assert sol.minMirrorPairDistance([12, 21, 45, 33, 54]) == 1
    assert sol.minMirrorPairDistance([21, 120]) == -1
    assert sol.minMirrorPairDistance([120, 21]) == 1
    assert sol.minMirrorPairDistance([12, 2, 21, 4, 66, 78, 21]) == 2
    print("Running Solution...")
