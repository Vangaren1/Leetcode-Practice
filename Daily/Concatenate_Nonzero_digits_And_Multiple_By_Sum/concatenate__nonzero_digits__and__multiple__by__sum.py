from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = 0
        place = 1
        x = 0
        while n:
            tmp = n % 10
            if tmp != 0:
                s += tmp
                x += tmp * place
                place *= 10
            n //= 10
        return x * s


if __name__ == "__main__":
    sol = Solution()
    n = 10203004
    print(sol.sumAndMultiply(n))
    print("Running Solution...")
