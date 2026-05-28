from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        hset = set()

        for first in arr1:
            while first:
                hset.add(first)
                first //= 10

        maxSeen = 0
        for second in arr2:
            while second:
                if second in hset:
                    maxSeen = max(maxSeen, len(str(second)))
                    break
                second = second // 10
        return maxSeen


if __name__ == "__main__":
    sol = Solution()
    arr1 = [1, 2, 3]
    arr2 = [4, 4, 4]
    print(sol.longestCommonPrefix(arr1, arr2))

    print("Running Solution...")
