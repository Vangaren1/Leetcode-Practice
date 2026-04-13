from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        nmap = defaultdict(list)
        for index, num in enumerate(nums):
            nmap[num].append(index)

        minfound = float("inf")
        for indexes in nmap.values():
            if len(indexes) > 2:
                ptr = 0
                while ptr < len(indexes) - 2:
                    i, j, k = indexes[ptr], indexes[ptr + 1], indexes[ptr + 2]
                    curr = abs(i - j) + abs(j - k) + abs(k - i)
                    minfound = min(curr, minfound)
                    ptr += 1

        return minfound if minfound < float("inf") else -1
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 1, 1, 3]
    print(sol.minimumDistance(nums))
    print("Running Solution...")
