from typing import Optional, List
import heapq
from collections import defaultdict
import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        # now str1 is shorter or equal
        l1 = len(str1)
        l2 = len(str2)

        g = math.gcd(l1, l2)
        # g is the theoretical largest length the gcd of strings could be

        return str1[:g]
        pass


if __name__ == "__main__":
    sol = Solution()
    str1 = "ABAB"
    str2 = "AB"
    print(sol.gcdOfStrings(str1, str2))
    str1 = "ABABAB"
    str2 = "ABAB"
    print(sol.gcdOfStrings(str1, str2))
    print("Running Solution...")
