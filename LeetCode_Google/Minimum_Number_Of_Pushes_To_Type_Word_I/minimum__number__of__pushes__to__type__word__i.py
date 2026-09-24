from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minimumPushes(self, word: str) -> int:
        total = 0

        for i in range(len(word)):
            total += i // 8 + 1

        return total


if __name__ == "__main__":
    sol = Solution()
    word = "xycdefghij"
    print(sol.minimumPushes(word))
    print("Running Solution...")
