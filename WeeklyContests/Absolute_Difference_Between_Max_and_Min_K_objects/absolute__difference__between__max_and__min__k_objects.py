from typing import Optional, List
import heapq


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        maxHeap = []
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, -num)
            heapq.heappush(maxHeap, num)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
                heapq.heappop(minHeap)

        return sum(maxHeap) - abs(sum(minHeap))


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 2, 2, 4]
    k = 2

    print(sol.absDifference(nums, k))
    print("Running Solution...")
