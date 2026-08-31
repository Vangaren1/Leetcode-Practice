from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        left, right = 0, len(nums) - 1

        while left <= right:

            # calculate the middle point
            mid = left + (right - left) // 2

            # if on the left end, and the next number is larger, then it's a peak
            if mid == 0:
                if nums[mid + 1] < nums[mid]:
                    return mid
                else:
                    left = mid + 1
                    continue
            # if its on the right end, and the previous number is smaller, then it's a peak
            elif mid == len(nums) - 1:
                if nums[mid - 1] < nums[mid]:
                    return mid
                else:
                    right = mid - 1

            # from here on, we're not at the end of the array
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] <= nums[mid] <= nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 1, 3, 5, 6, 4]

    print(sol.findPeakElement(nums))
    print("Running Solution...")
