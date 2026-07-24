from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:

            mid = left + (right - left) // 2
            # see if can be done with mid weights in x days
            d = 1
            currWeight = 0
            for weight in weights:
                if currWeight + weight > mid:
                    currWeight = weight
                    d += 1
                else:
                    currWeight += weight
            if d <= days:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    sol = Solution()
    weights = [2, 4, 6, 1, 3, 10]
    days = 4
    print(sol.shipWithinDays(weights, days))
    print("Running Solution...")
