from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        ptr = 0
        while ptr < len(nums):

            right -= nums[ptr]
            if left == right:
                return ptr
            left += nums[ptr]
            ptr += 1

        return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 1, -1]
    print(sol.pivotIndex(nums))
    print("Running Solution...")
