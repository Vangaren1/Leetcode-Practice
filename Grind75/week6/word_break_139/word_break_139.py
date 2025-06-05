from typing import Optional, List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [ False for _ in range(len(s)+1)]
        dp[len(s)] = True
        
        for index in range(len(s)-1, -1, -1):
            for word in wordDict:
                if (index + len(word)) <= len(s):
                    curr = s[index: index + len(word)]
                    if curr == word: 
                        dp[index] = dp[index + len(word)]
                if dp[index]:
                    break
        
        return dp[0]

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet","code"]
    sol = Solution()
    
    print(sol.wordBreak(s, wordDict))
    
    print("Running Solution...")
