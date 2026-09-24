from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        if k < numOnes:
            return k

        k -= numOnes
        if k < numZeros:
            return numOnes
        k -= numZeros

        return numOnes - k
        pass


if __name__ == "__main__":
    sol = Solution()
    numOnes = 3
    numZeros = 2
    numNegOnes = 0
    k = 2
    print(sol.kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))
    print("Running Solution...")
