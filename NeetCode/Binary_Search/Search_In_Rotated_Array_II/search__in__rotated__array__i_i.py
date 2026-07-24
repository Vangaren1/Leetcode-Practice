from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target or nums[left] == target or nums[right] == target:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            elif nums[left] < nums[mid]:
                # left half is sorted
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                # right half sorted
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 0, 1, 1, 1]
    target = 0
    print(sol.search(nums, target))
    print("Running Solution...")
