from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [set() for _ in range(n)]
        trusts = [set() for _ in range(n)]

        for a, b in trust:
            trusted[b - 1].add(a - 1)
            trusts[a - 1].add(b - 1)

        for index in range(n):
            if len(trusted[index]) == n - 1 and len(trusts[index]) == 0:
                return index + 1
        return -1

        pass


if __name__ == "__main__":
    sol = Solution()
    n = 1
    trust = []
    print(sol.findJudge(n, trust))
    print("Running Solution...")
