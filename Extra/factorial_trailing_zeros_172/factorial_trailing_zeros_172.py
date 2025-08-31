from typing import Optional, List


class Solution:
    def trailingZeroes(self, n: int) -> int:
        seen = {0: 1, 1: 1}

        def fact(n):
            if n in seen:
                return seen[n]
            return fact(n - 1) * n

        num = fact(n)

        c = 0
        while num % 10 == 0:
            num = num // 10
            c += 1
        return c


if __name__ == "__main__":
    sol = Solution()
    print(sol.trailingZeroes(5))
    print("Running Solution...")
