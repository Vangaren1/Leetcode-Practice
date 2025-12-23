from typing import Optional, List
import math
from collections import defaultdict


class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:

        subordinates = defaultdict(set)

        canDiscount = [False] * n

        for boss, sub in hierarchy:
            subordinates[boss].add(sub)

        dp = [future[i] - present[i] for i in range(n)]
        dp1 = [(future[i] - math.floor(present[i] / 2)) for i in range(n)]

        maxProfit = float("-inf")

        def dfs(index, currTotal, budgetRemaining):
            nonlocal maxProfit
            if index == n:
                return
            # determine the current profit
            maxProfit = max(maxProfit, currTotal)

            purchase = dp1[index] if canDiscount[index] else dp[index]
            cost = (
                math.floor(present[index] / 2) if canDiscount[index] else present[index]
            )

            if cost <= budgetRemaining:
                # test if the purchase is included
                for sub in subordinates[index + 1]:
                    canDiscount[sub - 1] = True

                dfs(index + 1, currTotal + purchase, budgetRemaining - cost)

            for sub in subordinates[index + 1]:
                canDiscount[sub - 1] = False
            # test if hte purchase is NOT included
            dfs(index + 1, currTotal, budgetRemaining)

        dfs(0, 0, budget)

        return maxProfit

        pass


if __name__ == "__main__":
    sol = Solution()

    n = 2
    present = [1, 2]
    future = [4, 3]
    hierarchy = [[1, 2]]
    budget = 3

    print(sol.maxProfit(n, present, future, hierarchy, budget))

    print("Running Solution...")
