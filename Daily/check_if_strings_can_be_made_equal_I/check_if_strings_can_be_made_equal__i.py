from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even1 = set()
        odd1 = set()
        even2 = set()
        odd2 = set()

        for i in range(len(s1)):
            if i % 2 == 0:
                even1.add(s1[i])
                even2.add(s2[i])
            else:
                odd1.add(s1[i])
                odd2.add(s2[i])
        return even1 == even2 and odd1 == odd2
        pass


if __name__ == "__main__":
    sol = Solution()

    s1 = "abcd"
    s2 = "cdab"
    print(sol.canBeEqual(s1, s2))

    s1 = "abcd"
    s2 = "dacb"
    print(sol.canBeEqual(s1, s2))
    print("Running Solution...")
