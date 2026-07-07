from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for index in range(1, len(prices)):
            price = prices[index]
            if price > prices[index - 1]:
                total += price - prices[index - 1]
        return total
        pass


if __name__ == "__main__":
    sol = Solution()
    prices = [1, 2, 3, 4, 5]
    print(sol.maxProfit(prices))
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices))
    print("Running Solution...")
