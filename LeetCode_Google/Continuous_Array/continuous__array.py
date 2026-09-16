from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ones = 0
        zeros = 0
        last = {0: -1}
        best = 0
        for index in range(n):
            if nums[index]:
                ones += 1
            else:
                zeros += 1
            diff = ones - zeros
            if diff in last:
                best = max(best, index - last[diff])
            else:
                last[diff] = index
        return best


if __name__ == "__main__":
    sol = Solution()

    nums = [0, 1]
    print(sol.findMaxLength(nums))

    # nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
    # print(sol.findMaxLength(nums))
    print("Running Solution...")
