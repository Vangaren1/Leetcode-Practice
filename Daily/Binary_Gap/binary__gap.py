from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def binaryGap(self, n: int) -> int:
        found = 0
        count = 0
        started = False
        while n:
            tmp = n % 2
            if tmp and not started:
                count += 1
                started = True
            elif tmp and started:
                found = max(found, count)
                count = 1
            elif started:
                count += 1
            n >>= 1
        return found


if __name__ == "__main__":
    sol = Solution()
    print(sol.binaryGap(6))
    print("Running Solution...")
