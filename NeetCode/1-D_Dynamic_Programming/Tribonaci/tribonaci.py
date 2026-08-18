from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n in (1, 2):
            return 1
        dp = [None for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]

        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.tribonacci(3))
    print(sol.tribonacci(21))
    print("Running Solution...")
