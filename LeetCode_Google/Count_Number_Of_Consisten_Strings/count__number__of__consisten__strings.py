from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = set(allowed)

        count = 0

        for word in words:
            ok = True
            for ch in word:
                if ch not in allow:
                    ok = False
            if ok:
                count += 1
        return count
        pass


if __name__ == "__main__":
    sol = Solution()
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    print(sol.countConsistentStrings(allowed, words))
    print("Running Solution...")
