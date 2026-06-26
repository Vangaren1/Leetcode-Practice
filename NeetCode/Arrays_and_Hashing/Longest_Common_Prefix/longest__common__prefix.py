from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if len(s) - 1 < i or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]


if __name__ == "__main__":
    sol = Solution()
    strs = ["ab", "a"]
    print(sol.longestCommonPrefix(strs))
    print("Running Solution...")
