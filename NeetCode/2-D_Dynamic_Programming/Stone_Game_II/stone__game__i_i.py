from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {}

        def dfs(alice, index, m):
            if index == n:
                return 0

            if (alice, index, m) in dp:
                return dp[(alice, index, m)]

            pileTotal = 0
            res = 0 if alice else float("inf")

            for x in range(1, 2 * m + 1):
                if index + x > n:
                    break

                pileTotal += piles[index + x - 1]
                # the amount alice takes
                if alice:
                    res = max(res, pileTotal + dfs(not alice, index + x, max(m, x)))
                else:
                    res = min(res, dfs(not alice, index + x, max(m, x)))

                dp[(alice, index, m)] = res
            return res

        return dfs(True, 0, 1)

        pass


if __name__ == "__main__":
    sol = Solution()
    piles = [3, 1, 2, 5, 7]
    print(sol.stoneGameII(piles))
    print("Running Solution...")
