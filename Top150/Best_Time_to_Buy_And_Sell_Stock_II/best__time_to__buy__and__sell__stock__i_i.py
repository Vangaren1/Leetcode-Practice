from typing import Optional, List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lastBuy = prices[0]
        ptr = 0
        n = len(prices)
        total = 0

        while ptr < n - 1:
            curr = prices[ptr]
            nextPrice = prices[ptr + 1]

            if nextPrice < curr:
                total += curr - lastBuy
                lastBuy = nextPrice
            elif lastBuy < nextPrice and ptr == n - 2:
                total += nextPrice - lastBuy

            ptr += 1

        return total

        pass


if __name__ == "__main__":
    sol = Solution()
    prices = [6, 1, 3, 2, 4, 7]
    expected = 7
    print(sol.maxProfit(prices))
    print("Running Solution...")
