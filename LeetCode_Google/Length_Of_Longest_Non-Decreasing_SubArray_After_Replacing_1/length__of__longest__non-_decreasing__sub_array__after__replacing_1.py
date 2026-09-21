from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        fromLeft = [1] * n
        fromRight = [1] * n

        for index in range(1, n):
            if nums[index] >= nums[index - 1]:
                fromLeft[index] = fromLeft[index - 1] + 1

        for index in range(n - 2, -1, -1):
            if nums[index] <= nums[index + 1]:
                fromRight[index] = fromRight[index + 1] + 1

        currMax = max(fromLeft)

        # test each index to see if replacing that would improve the best link

        for index in range(n):

            # see if replacing this index can extend a subarray length backwards
            if index > 0:
                currMax = max(currMax, fromLeft[index - 1] + 1)

            # see if we can extend to the right
            if index < n - 1:
                currMax = max(currMax, fromRight[index + 1] + 1)

            if 0 < index < n - 1 and nums[index - 1] <= nums[index + 1]:
                currMax = max(currMax, fromLeft[index - 1] + fromRight[index + 1] + 1)

        return currMax


if __name__ == "__main__":
    sol = Solution()
    nums = [6, -4, -1, -1]
    print(sol.longestSubarray(nums))
    print("Running Solution...")
