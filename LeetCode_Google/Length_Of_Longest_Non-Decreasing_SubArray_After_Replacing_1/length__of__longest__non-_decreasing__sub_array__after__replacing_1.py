from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        decreasing = [1 for _ in range(n)]
        maxSeen = [nums[0]]

        for i in range(1, n):
            maxSeen.append(max(nums[i], maxSeen[-1]))
            if nums[i] < nums[i - 1]:
                decreasing[i] = 0

        print(decreasing)
        print(maxSeen)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1, 2]
    print(sol.longestSubarray(nums))
    print("Running Solution...")
