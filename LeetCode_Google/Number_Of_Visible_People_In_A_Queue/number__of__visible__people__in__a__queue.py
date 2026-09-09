from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        dp = [0] * n

        stk = []

        for index in range(n - 1, -1, -1):
            while stk and stk[-1] < heights[index]:
                stk.pop()
                dp[index] += 1

            if stk:
                dp[index] += 1

            stk.append(heights[index])

        return dp


if __name__ == "__main__":
    sol = Solution()
    heights = [10, 1, 2, 3, 7, 6, 5, 4, 11]
    print(sol.canSeePersonsCount(heights))
    print("Running Solution...")
