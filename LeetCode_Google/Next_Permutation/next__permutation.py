from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(a, b):
            while a < b:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b -= 1

        # find pivot
        left = len(nums) - 2

        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1

        # if no pivot exists, return original
        if left < 0:
            reverse(0, len(nums) - 1)
            return nums

        # find largest index l with l>k such that nums[k] < nums[l]
        right = left + 1
        for tmp in range(right, len(nums)):
            if nums[left] < nums[tmp]:
                right = tmp

        nums[left], nums[right] = nums[right], nums[left]

        # reverse left + 1 to the end

        r1 = left + 1
        r2 = len(nums) - 1
        reverse(r1, r2)


if __name__ == "__main__":
    sol = Solution()

    nums = [4, 3, 2, 5, 4, 3, 1]
    print(sol.nextPermutation(nums))
    print("Running Solution...")
