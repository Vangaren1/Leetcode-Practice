from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        def bestScore(alice, bob, aliceTurn, ptr):
            if ptr >= len(stoneValue):
                return (alice, bob)
            take1 = stoneValue[ptr : ptr + 1]
            take2 = stoneValue[ptr : ptr + 2]
            take3 = stoneValue[ptr : ptr + 3]
            s1, s2, s3 = sum(take1), sum(take2), sum(take3)

            if aliceTurn:
                test1 = bestScore(alice + s1, bob, not aliceTurn, ptr + 1)
                test2 = bestScore(alice + s2, bob, not aliceTurn, ptr + 2)
                test3 = bestScore(alice + s3, bob, not aliceTurn, ptr + 3)
                return max([test1, test2, test3], key=lambda x: x[0])
            else:
                test1 = bestScore(alice, bob + s1, not aliceTurn, ptr + 1)
                test2 = bestScore(alice, bob + s2, not aliceTurn, ptr + 2)
                test3 = bestScore(alice, bob + s3, not aliceTurn, ptr + 3)
                return max([test1, test2, test3], key=lambda x: x[1])

        alice, bob = bestScore(0, 0, True, 0)
        if alice == bob:
            return "Tie"
        if alice > bob:
            return "Alice"
        return "Bob"


if __name__ == "__main__":
    sol = Solution()
    print(sol.stoneGameIII([1, 2, 3, 7]))
    print("Running Solution...")
