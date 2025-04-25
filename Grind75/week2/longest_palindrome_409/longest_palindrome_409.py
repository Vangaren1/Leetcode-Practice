from typing import Optional
from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        for ch in s:
            count[ch] += 1
        found1 = False
        total = 0
        for value in count.values():
            total += value - (value % 2)
            if value % 2 == 1 and not found1:
                total += 1
                found1 = True
        return total
    

if __name__ == "__main__":
    s = "abccccdd"
    sol = Solution()
    print(sol.longestPalindrome(s))
    print("Running Solution...")
