from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        maxSeen = -1
        right = 0

        for left in range(n):
            right = max(left, right)
            while right < n and nums[right] <= nums[left] * k:
                right += 1
            maxSeen = max(maxSeen, right - left)

        return n - maxSeen

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 6, 2, 9]
    k = 3
    print(sol.minRemoval(nums, k))
    print("Running Solution...")
