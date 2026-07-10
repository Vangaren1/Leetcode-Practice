from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 10, 10, 30, 30, 30]
    print(sol.removeDuplicates(nums))
    print(nums)
    print("Running Solution...")
