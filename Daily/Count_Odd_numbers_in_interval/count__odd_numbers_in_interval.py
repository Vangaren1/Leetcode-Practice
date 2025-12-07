from typing import Optional, List


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low + 1
        if low % 2 == 0:
            diff -= 1
        if high % 2 == 1:
            diff += 1

        return diff // 2


if __name__ == "__main__":
    sol = Solution()
    low = 3
    high = 7
    print(sol.countOdds(low, high))
    low = 0
    high = 10
    print(sol.countOdds(low, high))
    print("Running Solution...")
