from typing import Optional, List
import heapq
from collections import defaultdict
import string


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [0] * 26
        upper = [0] * 26
        for ch in word:
            if ch in string.ascii_lowercase:
                lower[ord(ch) - ord("a")] |= 1
            else:
                upper[ord(ch) - ord("A")] |= 1
        total = 0
        for i in range(26):
            if lower[i] and upper[i]:
                total += 1
        return total


if __name__ == "__main__":
    sol = Solution()
    word = "abc"
    print(sol.numberOfSpecialChars(word))
    print("Running Solution...")
