from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        curr = 0
        best = 0

        for g in gain:
            curr += g
            best = max(best, curr)
        return best
        pass


if __name__ == "__main__":
    sol = Solution()
    gain = [-5, 1, 5, 0, -7]
    print(sol.largestAltitude(gain))
    print("Running Solution...")
