from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        ptr1 = 0
        ptr2 = k
        nums.sort()
        minFound = float("inf")
        while ptr2 <= len(nums):
            tmp = nums[ptr1:ptr2]
            minFound = min(minFound, max(tmp) - min(tmp))
            ptr1 += 1
            ptr2 += 1
        return minFound


if __name__ == "__main__":
    sol = Solution()
    nums = [9, 4, 1, 7]
    print(sol.minimumDifference(nums, 2))
    print("Running Solution...")
