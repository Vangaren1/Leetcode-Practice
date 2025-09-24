from typing import Optional, List
from collections import deque
import heapq


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hq = []

        maxFound = nums[0]
        minFound = nums[0]

        for i in range(n):
            left = nums[i]
            for j in range(i, n):
                right = nums[j]
                if i != j:
                    maxFound = max(maxFound, left, right)
                    minFound = min(minFound, left, right)
                    val = maxFound - minFound
                    heapq.heappush(hq, val)
                    if len(hq) > k:
                        heapq.heappop(hq)

        return sum(hq)


if __name__ == "__main__":
    sol = Solution()
    nums = [15, 50, 27]
    print(sol.maxTotalValue(nums, 2))

    nums = [11, 8]
    print(sol.maxTotalValue(nums, 2))
    print("Running Solution...")
