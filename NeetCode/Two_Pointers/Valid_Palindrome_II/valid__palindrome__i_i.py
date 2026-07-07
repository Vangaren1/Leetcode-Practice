from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palinSkip(n):
            left, right = 0, len(s)
            while left < right:
                if left == n:
                    left += 1
                elif right == n:
                    right -= 1
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        l, r = 0, len(s)
        while l < r:
            if s[l] != s[r]:
                return palinSkip(l) or palinSkip(r)
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    s = "abca"
    print(sol.validPalindrome(s))

    print("Running Solution...")
