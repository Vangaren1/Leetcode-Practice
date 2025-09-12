from typing import Optional, List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for index in range(len(s) + 1):
            if dp[-1]:
                break
            if dp[index]:
                for word in wordDict:
                    if s[index : (len(word) + index)] == word:
                        dp[len(word) + index] = dp[index]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    s = "neetcode"
    wordDict = ["neet", "code"]
    print(sol.wordBreak(s, wordDict))
    print("Running Solution...")
