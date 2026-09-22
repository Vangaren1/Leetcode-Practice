from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def reverseWords(self, s: str) -> str:
        wArr = s.split()
        return " ".join(wArr[::-1])
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "the sky is blue"
    print(sol.reverseWords(s))
    s = "  hello world  "
    print(sol.reverseWords(s))
    print("Running Solution...")
