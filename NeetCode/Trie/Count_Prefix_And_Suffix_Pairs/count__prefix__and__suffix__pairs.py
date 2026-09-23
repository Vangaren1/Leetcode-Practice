from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            return str2.startswith(str1) and str2.endswith(str1)

        count = 0
        for i in range(len(words)):
            curr = words[i]
            for j in range(i + 1, len(words)):
                word = words[j]
                if isPrefixAndSuffix(curr, word):
                    count += 1
        return count

        pass


if __name__ == "__main__":
    sol = Solution()
    words = ["a", "aba", "ababa", "aa"]
    print(sol.countPrefixSuffixPairs(words))
    print("Running Solution...")
