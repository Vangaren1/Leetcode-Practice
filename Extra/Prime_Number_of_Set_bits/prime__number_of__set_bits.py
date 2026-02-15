from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2, 3, 5, 7, 11, 13, 17, 19])

        count = 0
        for i in range(left, right + 1):
            if i.bit_count() in primes:
                count += 1
        return count

        pass


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
