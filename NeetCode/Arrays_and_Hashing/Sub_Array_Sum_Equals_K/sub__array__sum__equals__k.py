from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1

        curr, count = 0, 0
        for num in nums:
            curr += num
            if curr - k in freq:
                count += freq[curr - k]
            freq[curr] += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    nums = [2, -1, 1, 2]
    k = 2
    print(sol.subarraySum(nums, k))
    print("Running Solution...")
