from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:

        best = 0

        def backtrack(index, oneCount, zeroCount, setSize):
            nonlocal best
            if oneCount > n or zeroCount > m:
                return

            if index >= len(strs):
                return

            one = strs[index].count("1")
            zero = strs[index].count("0")

            if one + oneCount <= n and zero + zeroCount <= m:
                best = max(best, setSize + 1)

            # check if we include this in the set
            backtrack(index + 1, one + oneCount, zero + zeroCount, setSize + 1)

            # check if we do not include this in the set
            backtrack(index + 1, oneCount, zeroCount, setSize)

        backtrack(0, 0, 0, 0)
        return best


if __name__ == "__main__":
    sol = Solution()
    strs = ["10", "0001", "111001", "1", "0"]
    m = 4
    n = 3
    print(sol.findMaxForm(strs, m, n))
    print("Running Solution...")
