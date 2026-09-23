from typing import Optional, List
import heapq
from collections import defaultdict
import bisect


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1]

        first = bisect.bisect_left(nums, target)
        last = bisect.bisect_right(nums, target) - 1

        if first == len(nums):
            return [-1, -1]

        if nums[first] == target and nums[last] == target:
            return [first, last]

        return [-1, -1]
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(sol.searchRange(nums, target))

    print("Running Solution...")
