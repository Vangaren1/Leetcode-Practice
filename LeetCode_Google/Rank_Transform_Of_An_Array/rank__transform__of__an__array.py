from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        ranking = [(num, index) for index, num in enumerate(arr)]
        ranking.sort()

        r = [0] * len(arr)

        nSet = set(arr)
        nSetArr = [n for n in nSet]
        nSetArr.sort()
        rankingNum = {val: index + 1 for index, val in enumerate(nSetArr)}

        for num, index in ranking:
            r[index] = rankingNum[num]

        return r
        pass


if __name__ == "__main__":
    sol = Solution()
    arr = [40, 10, 20, 30]
    print(sol.arrayRankTransform(arr))
    print("Running Solution...")
