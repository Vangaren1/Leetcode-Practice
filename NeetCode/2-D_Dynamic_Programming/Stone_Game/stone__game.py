from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        memo = {}

        def dfs(left, right):
            if left == right:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]

            takeleft = piles[left] - dfs(left + 1, right)
            takeright = piles[right] - dfs(left, right - 1)

            memo[(left, right)] = max(takeleft, takeright)
            return memo[(left, right)]

        return dfs(0, len(piles) - 1) > 0

        pass


if __name__ == "__main__":
    sol = Solution()
    piles = [1, 2, 3, 1]
    print(sol.stoneGame(piles))
    print("Running Solution...")
