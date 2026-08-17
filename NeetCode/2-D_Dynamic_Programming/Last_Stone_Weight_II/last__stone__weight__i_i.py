from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stonesum = sum(stones)
        target = stonesum // 2
        memo = {}

        def dfs(index, total):
            if index == len(stones) or total >= target:
                return abs(total - (stonesum - total))

            if (index, total) in memo:
                return memo[(index, total)]
            memo[(index, total)] = min(
                dfs(index + 1, total + stones[index]), dfs(index + 1, total)
            )
            return memo[(index, total)]

        return dfs(0, 0)

        pass


if __name__ == "__main__":
    sol = Solution()
    stones = [2, 7, 4, 1, 8, 1]
    print(sol.lastStoneWeightII(stones))
    print("Running Solution...")
