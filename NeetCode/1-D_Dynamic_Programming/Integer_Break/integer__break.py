from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        if n == 5:
            return 6

        dp = [1 for _ in range(n + 1)]

        dp[2] = 1
        dp[3] = 2
        dp[4] = 4
        dp[5] = 6

        for i in range(6, n + 1):
            if i % 3 == 0:
                dp[i] = 3 * dp[i - 1] // 2
            elif i % 3 == 1:
                dp[i] = 4 * dp[i - 1] // 3
            else:
                dp[i] = 2 * dp[i - 2]
        return dp[n]

        pass


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")

""" 
2 = 1 + 1 => 1 * 1 = 1 
3 = 1 + 2 => 1 * 2 = 2
4 = 2 + 2 => 2 * 2 = 4
5 = 3 + 2 => 3 * 2 = 6

6 = 3 + 3 => 3 * 3 = 9
7 = 3 + 4 => 3 * 4= 12
8 = 3 + 3 + 2 => 3 * 3 * 2 = 18
9 = 3 + 3 + 3 => 3 * 3 * 3 = 27
10 = 3 + 3 + 4 => 3 * 3 * 4 = 36 
11 = 3 + 3 + 3 + 2 => 3 * 3 * 3 * 2 = 54
12 = 3 + 3 + 3 + 3 => 3 * 3 * 3 * 3 = 81

if(n% 3 == 0) dp[i] = dp[i-1]/2 * 3;
if(n%3 == 1) dp[i] = dp[i-1]/3 * 4;
if(n%3 == 2) dp[i] = dp[i-2] * 2;
"""
