from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 1

        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))

        # sort if they're not already
        if minIndex > maxIndex:
            minIndex, maxIndex = maxIndex, minIndex
        # find which one is closer to the front or back

        fromFront = maxIndex + 1
        fromBack = n - minIndex
        fromBothSides = (minIndex + 1) + (n - maxIndex)

        return min(fromFront, fromBack, fromBothSides)

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 10, 7, 5, 4, 1, 8, 6]
    print(sol.minimumDeletions(nums))

    # nums = [0, 1, 2, 3, 4, 6, 7, 9, 10, -4, 19, 1, 8, -2, -3, 5]
    # print(sol.minimumDeletions(nums))
    print("Running Solution...")
