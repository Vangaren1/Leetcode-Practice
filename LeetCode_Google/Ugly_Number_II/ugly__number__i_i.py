from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        i2 = i3 = i5 = 0

        for i in range(1, n):
            next2 = dp[i2] * 2
            next3 = dp[i3] * 3
            next5 = dp[i5] * 5

            dp[i] = min(next2, next3, next5)

            if next2 == dp[i]:
                i2 += 1
            if next3 == dp[i]:
                i3 += 1
            if next5 == dp[i]:
                i5 += 1
        return dp[n - 1]

        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.nthUglyNumber(1690))

    print("Running Solution...")
