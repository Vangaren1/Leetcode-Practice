from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if mid > 0 and nums[mid - 1] < target:
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1
        return mid


if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 2, 4, 6, 8]
    target = 5
    print(sol.searchInsert(nums, target))
    print("Running Solution...")
