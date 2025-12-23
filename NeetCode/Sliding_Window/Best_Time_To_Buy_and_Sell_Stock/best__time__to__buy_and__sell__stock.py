from typing import Optional, List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        h = [float("-inf")] * n
        l = [float("inf")] * n

        h[0] = prices[0]
        l[-1] = prices[-1]

        for i in range(1, n):
            h[i] = max(prices[i], h[i - 1])
            l[-i - 1] = min(prices[-i - 1], l[-i])

        maxProfit = 0
        for j in range(n):
            curr = prices[j]
            currProfit = h[j]
            if currProfit - curr > 0:
                maxProfit = max(maxProfit, currProfit)

        return maxProfit


if __name__ == "__main__":
    sol = Solution()
    prices = [10, 1, 5, 6, 7, 1]
    expected = 6
    print(sol.maxProfit(prices))
    print("Running Solution...")


"""
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

        """
