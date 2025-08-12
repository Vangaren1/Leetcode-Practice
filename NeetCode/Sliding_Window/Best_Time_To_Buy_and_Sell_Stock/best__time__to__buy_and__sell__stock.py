from typing import Optional, List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float("inf")

        lowest = min(prices[0], lowest)
        mxP = 0
        for index in range(len(prices)):
            p = prices[index] - lowest
            if p > 0:
                mxP = max(mxP, p)
            lowest = min(prices[index], lowest)
        return mxP


if __name__ == "__main__":
    sol = Solution()
    prices = [10, 1, 5, 6, 7, 1]
    expected = 6
    print(sol.maxProfit(prices))
    print("Running Solution...")
