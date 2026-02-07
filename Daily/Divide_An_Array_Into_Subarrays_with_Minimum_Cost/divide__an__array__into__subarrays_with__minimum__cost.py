from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        queue = []

        total = nums[0]

        for num in nums[1:]:
            heapq.heappush(queue, num)

        total += heapq.heappop(queue)
        total += heapq.heappop(queue)
        return total


if __name__ == "__main__":
    sol = Solution()
    nums = [10, 3, 1, 1]
    print(sol.minimumCost(nums))
    print("Running Solution...")
