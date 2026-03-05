from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minOperations(self, s: str) -> int:
        total, zC, oC = 0, 0, 0
        sZ = True
        for ch in s:
            if sZ:
                if ch == "0":
                    oC += 1
                else:
                    zC += 1
            else:
                if ch == "0":
                    zC += 1
                else:
                    oC += 1
            total = min(zC, oC)
        return total


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
