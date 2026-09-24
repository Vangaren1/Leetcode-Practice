from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def dprod(i):
            curr = 1

            while i:
                curr *= i % 10
                i //= 10
            return curr

        while dprod(n) % t != 0:
            n += 1
        return n
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestNumber(10, 2))
    print(sol.smallestNumber(15, 3))
    print("Running Solution...")
