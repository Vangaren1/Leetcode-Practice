from typing import Optional, List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            total = 0
            for p in piles:
                total += (p + mid - 1) / mid
            if total <= h:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    sol = Solution()

    piles = [25, 10, 23, 4]
    h = 4

    print(sol.minEatingSpeed(piles, h))
    print("Running Solution...")
