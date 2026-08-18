from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        def binary(left, right):
            if left == right:
                if left == 0 or right == len(nums) - 1:
                    return -1
                if left > 0 and right < len(nums) - 1:
                    if nums[left - 1] < nums[left] < nums[left + 1]:
                        return left
                    return -1
            mid = left + (right - left) // 2

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 1, 3, 5, 6, 4]

    print(sol.findPeakElement(nums))
    print("Running Solution...")
