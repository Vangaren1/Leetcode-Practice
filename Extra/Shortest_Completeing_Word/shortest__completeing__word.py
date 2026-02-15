from typing import Optional, List
import heapq, string
from collections import defaultdict, Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = [c for c in licensePlate.lower() if c in string.ascii_lowercase]

        def check(src, target):
            return not (Counter(src) - Counter(target))

        foundW = None
        for word in words:
            if check(letters, [ch for ch in word]):
                if not foundW or len(word) < len(foundW):
                    foundW = word
        return foundW


if __name__ == "__main__":
    sol = Solution()
    licensePlate = "1s3 PSt"
    words = ["step", "steps", "stripe", "stepple"]
    print(sol.shortestCompletingWord(licensePlate, words))
    print("Running Solution...")
