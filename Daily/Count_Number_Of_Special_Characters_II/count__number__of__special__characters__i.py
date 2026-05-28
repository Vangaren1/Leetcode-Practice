from typing import Optional, List
import heapq
from collections import defaultdict
import string


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()
        exclude = set()

        for ch in word:
            if ch not in exclude:
                if ch in string.ascii_lowercase:
                    lower.add(ch)
                    if ch.upper() in upper:
                        exclude.add(ch)
                        exclude.add(ch.upper())
                        upper.remove(ch.upper())
                elif ch in string.ascii_uppercase:
                    if ch.lower() in lower:
                        upper.add(ch)
                    else:
                        exclude.add(ch)
                        exclude.add(ch.lower())

        return len(upper)


if __name__ == "__main__":
    sol = Solution()
    words = ["AbcbDBdD"]
    for w in words:
        print(sol.numberOfSpecialChars(w))
    print("Running Solution...")
