from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for index in range(len(s) // 2):
            s[index], s[-1 - index] = s[-1 - index], s[index]


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
