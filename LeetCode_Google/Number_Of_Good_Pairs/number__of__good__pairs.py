from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    count += 1
        return count

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1, 1, 3]
    print("Running Solution...")
