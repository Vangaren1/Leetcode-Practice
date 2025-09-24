from typing import Optional, List


class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0

        while n > 0:
            if n % 2 == 1:
                total += 1
            n = n >> 1
        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(2147483645))
    print("Running Solution...")
