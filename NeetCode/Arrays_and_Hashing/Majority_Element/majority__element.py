from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        n = len(nums)
        for num in nums:
            count[num] += 1
            if count[num] > n // 2:
                return num


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
