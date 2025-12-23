from typing import Optional, List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        highest = [float("-inf")] * n
        lowest = [float("inf")] * n

        highest[0] = prices[0]
        lowest[-1] = prices[-1]
        for idx in range(1, n):
            highest[idx] = max(prices[idx], highest[idx - 1])
            lowest[-idx - 1] = min(prices[-idx - 1], lowest[-idx])

        def dfs(idx: int, total: int, short: bool, inProgress: bool, remaining: int):
            if remaining == 0:
                if not inProgress:
                    return total 
                if short:
                    
            
            

            pass


if __name__ == "__main__":
    sol = Solution()
    prices = [1, 7, 9, 8, 2]
    k = 2
    print(sol.maximumProfit(prices, k))
    print("Running Solution...")
