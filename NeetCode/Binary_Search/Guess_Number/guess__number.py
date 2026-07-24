from typing import Optional, List
import heapq
from collections import defaultdict


# def guess(num: int) -> int:
def guess(num: int) -> int:
    i = 7
    print(f"guessing {num}")
    if num == i:
        return 0
    if num > i:
        return -1
    return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g == -1:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.guessNumber(10))
    print("Running Solution...")
