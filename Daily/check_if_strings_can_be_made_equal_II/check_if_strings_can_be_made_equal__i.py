from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1 = [0] * 26
        even2 = [0] * 26
        odd1 = [0] * 26
        odd2 = [0] * 26
        for index in range(len(s1)):
            if index % 2 == 0:
                even1[ord(s1[index]) - ord("a")] += 1
                even2[ord(s2[index]) - ord("a")] += 1
            else:
                odd1[ord(s1[index]) - ord("a")] += 1
                odd2[ord(s2[index]) - ord("a")] += 1
        return even1 == even2 and odd1 == odd2


if __name__ == "__main__":
    sol = Solution()

    s1 = "abcd"
    s2 = "cdab"
    print(sol.checkStrings(s1, s2))

    s1 = "abcd"
    s2 = "dacb"
    print(sol.checkStrings(s1, s2))
    print("Running Solution...")
