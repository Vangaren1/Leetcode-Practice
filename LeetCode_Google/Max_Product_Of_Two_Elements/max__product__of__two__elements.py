from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
        pass


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
