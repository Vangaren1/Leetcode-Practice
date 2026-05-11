from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        step = 0
        while step < n:
            if (
                words[(startIndex + step) % n] == target
                or words[(startIndex + n - step) % n] == target
            ):
                return step
            step += 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    words = ["hello", "i", "am", "leetcode", "hello"]
    target = "hello"
    startIndex = 1
    print(sol.closestTarget(words, target, startIndex))
    print("Running Solution...")
