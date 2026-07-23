from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        curr = {}

        for index, val in enumerate(nums):
            if val in curr:
                if abs(index - curr[val]) <= k:
                    return True
            curr[val] = index

        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    print(sol.containsNearbyDuplicate(nums, k))
    print("Running Solution...")
