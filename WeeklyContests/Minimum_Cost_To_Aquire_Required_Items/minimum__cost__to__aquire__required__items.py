from typing import Optional, List


class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        reqBoth = max(need1, need2)
        useBoth = reqBoth * costBoth

        buyIndividual = cost1 * need1 + cost2 * need2

        reqMin = min(need1, need2)
        mix3 = costBoth * reqMin

        if need1 > need2:
            mix3 += cost1 * (need1 - reqMin)
        else:
            mix3 += cost2 * (need2 - reqMin)

        return min(buyIndividual, useBoth, mix3)


if __name__ == "__main__":
    sol = Solution()

    cost1 = 3
    cost2 = 2
    costBoth = 1
    need1 = 3
    need2 = 2
    # print(sol.minimumCost(cost1, cost2, costBoth, need1, need2))

    print(sol.minimumCost(50, 55, 72, 5, 3))

    # print(sol.minimumCost(5, 4, 15, 0, 0))

    # print(sol.minimumCost(5, 400, 15, 40, 30))
    print("Running Solution...")
