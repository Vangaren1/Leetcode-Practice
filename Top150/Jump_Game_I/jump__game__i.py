from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for index, num in enumerate(nums):
            if dp[-1]:
                return True
            for i in range(num):
                if (index + i + 1) < n:
                    dp[index + i + 1] = dp[index] or dp[index + i + 1]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 1, 0, 4]
    print(sol.canJump(nums))
    print("Running Solution...")
