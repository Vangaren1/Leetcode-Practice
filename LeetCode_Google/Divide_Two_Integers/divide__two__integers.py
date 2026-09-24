from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        for i in range(31, -1, -1):
            if (divisor << i) <= dividend:
                dividend -= divisor << i
                quotient |= 1 << i

        if negative:
            return ~quotient + 1

        return quotient

        pass


if __name__ == "__main__":
    sol = Solution()
    dividend = 10
    divisor = 3
    print(sol.divide(dividend, divisor))
    print("Running Solution...")
