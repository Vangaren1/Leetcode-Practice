from typing import Optional, List
import heapq
from collections import defaultdict


# 2147483647
class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        count = 9
        start = 1

        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10

        numberOffset = (n - 1) // digits
        number = start + numberOffset
        digit_index = (n - 1) % digits
        return int(str(number)[digit_index])


if __name__ == "__main__":
    sol = Solution()
    for i in (3, 11, 27):
        print(sol.findNthDigit(i))
    print("Running Solution...")
