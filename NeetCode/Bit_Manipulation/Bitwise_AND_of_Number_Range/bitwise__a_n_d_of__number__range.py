from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        msbIndexLeft = left.bit_length() - 1
        msbIndexRight = right.bit_length() - 1

        total = 0
        while msbIndexLeft >= 0:
            mask = 1 << msbIndexRight
            msbIndexRight -= 1
            msbIndexLeft -= 1
            lmask = left & mask
            rmask = right & mask
            if lmask != rmask:
                break
            total |= lmask
        return total


if __name__ == "__main__":
    sol = Solution()
    # left = 1
    # right = 2147483647
    # print(sol.rangeBitwiseAnd(left, right))

    left = 1
    right = 1
    print(sol.rangeBitwiseAnd(left, right))
    print("Running Solution...")
