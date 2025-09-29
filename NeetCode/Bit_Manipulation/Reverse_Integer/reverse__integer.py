from typing import Optional, List


class Solution:
    def reverse(self, x: int) -> int:
        MAXINT = 2**32 - 1
        MININT = -(2**31)

        res = 0

        while x not in (0, -1):

            if x > MAXINT // 10:
                return 0
            if x < MININT // 10:
                return 0

            res *= 10

            neg = False
            if x < 0:
                neg = True
                x *= -1

            res += x % 10
            x = x // 10

            if neg:
                x *= -1
        if neg and x == -1:
            res *= -10
            res -= 1

        return res


# [-2^31, 2^31 - 1]

if __name__ == "__main__":
    sol = Solution()
    x = -1234
    print(sol.reverse(x))
    print("Running Solution...")
