from typing import Optional, List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def rec(index, canBuy):
            if index >= len(prices):
                return 0

            if (index, canBuy) in cache:
                return cache[(index, canBuy)]

            curr = prices[index]
            cool = rec(index + 1, canBuy)
            if canBuy:
                buyOrSell = rec(index + 1, not canBuy) - curr
            else:
                buyOrSell = rec(index + 2, not canBuy) + curr
            cache[((index, canBuy))] = max(cool, buyOrSell)
            return cache[((index, canBuy))]

        return rec(0, True)


if __name__ == "__main__":
    sol = Solution()
    prices = [1, 3, 4, 0, 4]
    print(sol.maxProfit(prices))
    print("Running Solution...")
