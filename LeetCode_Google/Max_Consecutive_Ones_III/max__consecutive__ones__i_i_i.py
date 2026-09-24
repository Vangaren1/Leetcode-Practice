from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        window = {1: 0, 0: 0}
        n = len(nums)

        right = 0
        while right < n and window[0] < k:
            window[nums[right]] += 1
            right += 1

        best = right

        left = 0

        while right < n:
            best = max(best, right - left)
            window[nums[right]] += 1
            while window[0] > k:
                window[nums[left]] -= 1
                left += 1
            right += 1
        best = max(best, right - left)
        return best


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 0, 1, 1]
    k = 1
    print(sol.longestOnes(nums, k))
    print("Running Solution...")
