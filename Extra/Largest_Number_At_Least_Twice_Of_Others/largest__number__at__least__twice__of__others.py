from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        queue = []
        for index, num in enumerate(nums):
            heapq.heappush(queue, (-num, index))
        largest, idx = heapq.heappop(queue)
        second, idx2 = heapq.heappop(queue)

        return idx if abs(largest) >= abs(second) * 2 else -1

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 6, 1, 0]
    print(sol.dominantIndex(nums))
    nums = [1, 2, 3, 4]
    print(sol.dominantIndex(nums))
    print("Running Solution...")
