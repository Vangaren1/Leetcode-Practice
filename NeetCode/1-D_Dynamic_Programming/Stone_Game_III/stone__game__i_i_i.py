from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [None for _ in range(n)]
        dp[-1] = stoneValue[-1]

        def dfs(index):
            if index >= n:
                return 0

            if dp[index] is not None:
                return dp[index]

            options = []
            if index <= n - 1:
                options.append(stoneValue[index] - dfs(index + 1))
            if index <= n - 2:
                options.append(
                    stoneValue[index] + stoneValue[index + 1] - dfs(index + 2)
                )
            if index <= n - 3:
                options.append(
                    stoneValue[index]
                    + stoneValue[index + 1]
                    + stoneValue[index + 2]
                    - dfs(index + 3)
                )
            dp[index] = max(options)
            return dp[index]

        score = dfs(0)
        if score == 0:
            return "Tie"
        if score > 0:
            return "Alice"
        if score < 0:
            return "Bob"


if __name__ == "__main__":
    sol = Solution()
    print(sol.stoneGameIII([2, 4, 3, 1]))
    print(sol.stoneGameIII([1, 2, 1, 5]))
    print("Running Solution...")


""" 
# Works but is inefficient

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        def bestScore(alice, bob, aliceTurn, ptr):
            if ptr >= len(stoneValue):
                return (alice, bob)
            take1 = stoneValue[ptr : ptr + 1]
            take2 = stoneValue[ptr : ptr + 2]
            take3 = stoneValue[ptr : ptr + 3]
            s1, s2, s3 = sum(take1), sum(take2), sum(take3)

            if aliceTurn:
                test1 = bestScore(alice + s1, bob, not aliceTurn, ptr + 1)
                test2 = bestScore(alice + s2, bob, not aliceTurn, ptr + 2)
                test3 = bestScore(alice + s3, bob, not aliceTurn, ptr + 3)
                return max([test1, test2, test3], key=lambda x: x[0])
            else:
                test1 = bestScore(alice, bob + s1, not aliceTurn, ptr + 1)
                test2 = bestScore(alice, bob + s2, not aliceTurn, ptr + 2)
                test3 = bestScore(alice, bob + s3, not aliceTurn, ptr + 3)
                return max([test1, test2, test3], key=lambda x: x[1])

        alice, bob = bestScore(0, 0, True, 0)
        if alice == bob:
            return "Tie"
        if alice > bob:
            return "Alice"
        return "Bob"

"""
