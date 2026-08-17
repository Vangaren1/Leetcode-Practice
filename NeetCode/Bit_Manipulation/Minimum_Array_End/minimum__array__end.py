from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        xCount = x.bit_count()
        nCount = n.bit_length()
        totalBits = xCount + nCount
        xBits = bin(x)[2:]
        nBits = bin(n)[2:]
        xBits = xBits[::-1]
        nBits = nBits[::-1]
        xptr, nptr = 0, 0
        result = ""
        for bit in range(totalBits):
            if xBits[xptr] == "0":
                xptr += 1
            else:
                result += "1"
                continue
            result += nBits[nptr]
            nptr += 1

        return int(result[::-1], 2)

        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minEnd(5, 3))
    print("Running Solution...")
