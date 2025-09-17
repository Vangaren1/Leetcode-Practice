from typing import Optional, List
import heapq


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:

        seen = set()
        heap = []
        for num in nums:
            if num not in seen:
                seen.add(num)
                heapq.heappush(heap, num)
                if len(heap) > k:
                    heapq.heappop(heap)

        retList = []
        for _ in range(len(heap)):
            retList.append(heapq.heappop(heap))
        return retList[::-1]


if __name__ == "__main__":
    sol = Solution()
    nums = [84, 93, 100, 77, 93]
    print(sol.maxKDistinct(nums, 3))
    print("Running Solution...")
