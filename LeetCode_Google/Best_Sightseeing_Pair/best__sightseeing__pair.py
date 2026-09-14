from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        best = float("-inf")

        iArr = [float("-inf")] * n
        jArr = [float("-inf")] * n
        iArr[0] = values[0]
        jArr[n - 1] = values[n - 1] - (n - 1)
        for i in range(1, n):
            iArr[i] = max(iArr[i - 1], values[i] + i)
        for j in range(n - 2, -1, -1):
            jArr[j] = max(jArr[j + 1], values[j] - j)

        for index in range(n - 1):
            best = max(best, iArr[index] + jArr[index + 1])

        return best
        pass


if __name__ == "__main__":
    sol = Solution()
    values = [8, 1, 5, 2, 6]
    print(sol.maxScoreSightseeingPair(values))
    print("Running Solution...")


# values[i] + values[j] + i - j = score
