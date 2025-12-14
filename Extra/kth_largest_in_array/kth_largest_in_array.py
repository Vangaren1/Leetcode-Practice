from typing import Optional, List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []

        for num in nums:
            heapq.heappush(queue, -num)

        r = heapq.nsmallest(k, queue)

        return -r[-1]

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(sol.findKthLargest(nums, k))
    print("Running Solution...")
