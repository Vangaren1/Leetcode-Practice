from typing import Optional, List


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = n % 2
        n = n >> 1
        while n > 0:
            if n % 2 == last:
                return False
            last = n % 2
            n = n >> 1
        return True


if __name__ == "__main__":
    sol = Solution()

    assert sol.hasAlternatingBits(5) == True
    assert sol.hasAlternatingBits(7) == False
    print("Running Solution...")
