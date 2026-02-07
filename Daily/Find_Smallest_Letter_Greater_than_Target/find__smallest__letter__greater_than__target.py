from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        t = ord(target)
        minV = float("inf")
        if target != letters[0]:
            minC = letters[0]
        else:
            minC = letters[1]

        for letter in letters:
            curr = ord(letter) - t
            if curr > 0 and curr < minV:
                minV = curr
                minC = letter
        return minC


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreatestLetter(["c", "f", "j"], "c"))
    print("Running Solution...")
