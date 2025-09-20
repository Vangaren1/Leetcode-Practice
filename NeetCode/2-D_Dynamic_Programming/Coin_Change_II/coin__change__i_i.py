from typing import Optional, List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for index in range(coin, amount + 1):
                dp[index] = dp[index] + dp[index - coin]
        return dp[amount]


if __name__ == "__main__":
    sol = Solution()
    amount = 7
    coins = [2, 4]
    print(sol.change(amount, coins))
    print("Running Solution...")
