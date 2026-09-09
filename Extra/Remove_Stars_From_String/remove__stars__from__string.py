from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def removeStars(self, s: str) -> str:
        stk = []

        for ch in s:
            if ch == "*" and stk:
                stk.pop()
            else:
                stk.append(ch)

        return "".join(stk)


if __name__ == "__main__":
    sol = Solution()
    s = "leet**cod*e"
    print(sol.removeStars(s))
    print("Running Solution...")
