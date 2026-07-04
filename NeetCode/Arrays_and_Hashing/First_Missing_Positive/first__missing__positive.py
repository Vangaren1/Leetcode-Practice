from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        def hop(val):
            while nums[val - 1] != val:
                curr = nums[val - 1]
                nums[val - 1] = val
                if curr <= 0 or curr > n + 1:
                    break
                val = curr

        for index in range(len(nums)):
            if nums[index] <= 0 or nums[index] > n:
                nums[index] = 0
                continue
            hop(nums[index])

        for index in range(len(nums)):
            if nums[index] != index + 1:
                return index + 1
        return n + 1


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 4]
    print(sol.firstMissingPositive(nums))
    nums = [7, 8, 9, 10, 11]
    print(sol.firstMissingPositive(nums))
    nums = [1, 2, 4, 5, 6, 3, 1]
    print(sol.firstMissingPositive(nums))
    print("Running Solution...")
