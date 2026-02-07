from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def check(n):
            if 1 <= n <= 9:
                return True
            tmp = n

            while tmp > 0:
                d = tmp % 10
                if d == 0 or n % d != 0:
                    return False
                tmp -= d
                tmp /= 10
            return True

        retVal = []
        for i in range(left, right + 1):
            if check(i):
                retVal.append(i)
        return retVal

        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.selfDividingNumbers(1, 22))
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    print("Running Solution...")
