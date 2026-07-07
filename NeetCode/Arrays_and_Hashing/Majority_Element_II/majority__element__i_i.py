from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        n = len(nums)
        return [key for key, val in count.items() if val * 3 > n]


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 2, 3, 2, 2, 2, 2, 5, 5, 5]
    print(sol.majorityElement(nums))
    print("Running Solution...")
