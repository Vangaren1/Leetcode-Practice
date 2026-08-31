from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        shortest = None

        count = 0
        right = 0

        for index in range(len(s)):
            right = index
            count = 0
            while right < len(s) and count < k:
                if s[right] == "1":
                    count += 1
                right += 1
            if count < k and right == len(s):
                continue
            curr = s[index:right]
            if (
                shortest is None
                or (len(shortest) > len(curr))
                or (len(shortest) == len(curr) and shortest > curr)
            ):
                shortest = curr

        if shortest is None:
            return ""
        return shortest

        pass


if __name__ == "__main__":
    sol = Solution()
    s = "100011001"
    k = 3
    print(sol.shortestBeautifulSubstring(s, k))
    print("Running Solution...")
