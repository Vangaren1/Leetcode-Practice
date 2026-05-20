from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        aSet = set()
        bSet = set()
        results = []

        for index in range(len(A)):
            aSet.add(A[index])
            bSet.add(B[index])
            results.append(len(aSet & bSet))

        return results
        pass


if __name__ == "__main__":
    sol = Solution()
    A = [1, 3, 2, 4]
    B = [3, 1, 2, 4]
    print(sol.findThePrefixCommonArray(A, B))
    print("Running Solution...")
