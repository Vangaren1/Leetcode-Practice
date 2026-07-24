from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = left + (right - left) // 2
            peices = 1
            curr = 0
            for num in nums:
                if num + curr > mid:
                    peices += 1
                    curr = num
                else:
                    curr += num

            if peices <= k:
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    sol = Solution()
    nums = [7, 2, 5, 10, 8]
    k = 2
    print(sol.splitArray(nums, k))
    print("Running Solution...")
