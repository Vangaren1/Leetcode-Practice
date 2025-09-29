from typing import Optional, List


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x

        if n < 0:
            return 1 / self.myPow(x, abs(n))

        if n % 2 == 0:
            res = self.myPow(x, n // 2)
            return res * res

        return self.myPow(x, n - 1) * x


if __name__ == "__main__":
    sol = Solution()
    x = 2.00000
    n = 5
    print(sol.myPow(x, n))
    print("Running Solution...")
