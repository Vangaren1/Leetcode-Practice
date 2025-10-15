from typing import Optional, List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxVal = float("-inf")
        for acct in accounts:
            curr = sum(acct)
            maxVal = max(maxVal, curr)
        return maxVal

        pass


if __name__ == "__main__":
    sol = Solution()
    accounts = [[1, 2, 3], [3, 2, 1]]
    print(sol.maximumWealth(accounts))
    print("Running Solution...")
