from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        largest = 0
        n = len(nums)
        left = 0
        for right in range(n):
            counter[nums[right]] += 1
            while counter[nums[right]] > k:
                counter[nums[left]] -= 1
                left += 1
            largest = max(largest, right - left + 1)
        return largest
        pass


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 3, 1, 2, 3, 1, 2]
    k = 2
    print(sol.maxSubarrayLength(nums, k))
    print("Running Solution...")
