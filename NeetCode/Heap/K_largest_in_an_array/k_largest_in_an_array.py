from typing import Optional, List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kHeap = []
        for n in nums:
            heapq.heappush(kHeap, n)
            if len(kHeap) > k:
                heapq.heappop(kHeap)
        return kHeap[0]


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(sol.findKthLargest(nums, k))
    print("Running Solution...")
