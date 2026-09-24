from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()

        n = len(citations)

        count = defaultdict(int)

        best = 0
        for citation in citations:
            for j in range(1, n + 1):
                if citation >= j:
                    count[j] += 1

        for key, val in count.items():
            if val >= key:
                best = max(best, key)
        return best

        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.hIndex([3, 0, 6, 1, 5]))
    print(sol.hIndex([1]))
    print("Running Solution...")
