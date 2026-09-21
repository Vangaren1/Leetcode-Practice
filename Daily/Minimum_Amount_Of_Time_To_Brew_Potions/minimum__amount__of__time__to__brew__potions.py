from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        freeWhen = [0] * len(skill)

        for potion in mana:

            start = 0
            elapsed = 0

            for i in range(len(skill)):
                start = max(start, freeWhen[i] - elapsed)
                elapsed += skill[i] * potion

            elapsed = 0

            for i in range(len(skill)):
                elapsed += skill[i] * potion
                freeWhen[i] = start + elapsed

        return freeWhen[-1]
        pass


if __name__ == "__main__":
    sol = Solution()
    skill = [1, 5, 2, 4]
    mana = [5, 1, 4, 2]
    print(sol.minTime(skill, mana))
    print("Running Solution...")
