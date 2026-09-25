from typing import Optional, List
import heapq, math
from collections import defaultdict


# (2n)! / ((n+1)!n!)
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            total = 0
            for j in range(i):
                total += dp[j] * dp[i - 1 - j]
            dp[i] = total

        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    assert sol.numTrees(1) == 1
    assert sol.numTrees(2) == 2
    assert sol.numTrees(3) == 5
    print("Running Solution...")


""". 
# (2n)! / ((n+1)!n!)
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        
        top = math.factorial(2 * n)
        bottom = math.factorial(n)
        bottom *= bottom 
        bottom *= (n+1)
        return top//bottom 
"""
