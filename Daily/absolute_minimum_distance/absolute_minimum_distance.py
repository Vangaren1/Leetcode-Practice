from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        seen = defaultdict(list)

        ptr = 0
        while ptr < len(arr) - 1:
            b, a = arr[ptr + 1], arr[ptr]
            seen[b - a].append([a, b])
            ptr += 1

        return seen[min(seen.keys())]

        pass


if __name__ == "__main__":
    sol = Solution()
    arr = [4, 2, 1, 3]
    print(sol.minimumAbsDifference(arr))
    print("Running Solution...")
