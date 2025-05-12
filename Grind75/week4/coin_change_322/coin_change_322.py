from typing import Optional, List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [ amount + 1] * (amount + 2)
        dp[0] = 0
        for a in range(amount + 1):
            for c in coins: 
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a-c] + 1)
        return dp[amount] if dp[amount] != dp[amount + 1] else -1
    

if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    
    s = Solution()
    print(s.coinChange(coins, amount))
    print("Running Solution...")
