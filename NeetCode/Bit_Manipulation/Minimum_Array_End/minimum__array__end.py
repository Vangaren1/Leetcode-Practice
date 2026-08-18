from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        xmask = 1
        nmask = 1
        nbits = n.bit_length()
        xbits = x.bit_length()
        totalBits = nbits + xbits
        result = 0

        for _ in range(totalBits):
            currX = x & xmask
            currN = n & nmask

            if currX == 0:
                result |= currN

            else:
                result |= currX
                n <<= 1
            nmask <<= 1
            xmask <<= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.minEnd(97, 10000))
    # print(sol.minEnd(3, 2))
    print("Running Solution...")


"""  

100% works and passes, but i want to try this without bin()

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        xBits = bin(x)[2:]
        nBits = bin(n)[2:]
        xBits = xBits[::-1]
        nBits = nBits[::-1]
        totalBits = len(xBits) + len(nBits)
        xptr, nptr = 0, 0
        result = ""
        for bit in range(totalBits):
            if xptr < len(xBits):
                if xBits[xptr] == "0":
                    if nptr >= len(nBits):
                        result += "0"
                    xptr += 1
                else:
                    result += "1"
                    xptr += 1
                    continue
            if nptr < len(nBits):
                result += nBits[nptr]
                nptr += 1

        return int(result[::-1], 2)

"""
