from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minimumDeletions(self, s: str) -> int:
        aCount = s.count("a")
        bCount = 0
        minFound = aCount

        for ch in s:
            if ch == "a":
                aCount -= 1
            else:
                bCount += 1
            minFound = min(minFound, aCount + bCount)

        return minFound


if __name__ == "__main__":
    sol = Solution()
    s = "aababbab"
    print(sol.minimumDeletions(s))
    print("Running Solution...")
