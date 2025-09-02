from typing import Optional, List
from collections import defaultdict
import heapq


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s = str(n)
        c = defaultdict(int)
        for ch in s:
            c[ch] += 1

        h = []
        for key, value in c.items():
            heapq.heappush(h, (value, key))

        return int(heapq.heappop(h))


if __name__ == "__main__":
    sol = Solution()
    n = 1553322
    print(sol.getLeastFrequentDigit(n))
    print("Running Solution...")
