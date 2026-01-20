from typing import Optional, List
from collections import defaultdict
import math


class Solution:
    div = defaultdict(list)

    def divisors(self, num) -> list:
        if num in self.div:
            return self.div[num]

        retVal = []
        sq = math.isqrt(num)
        for i in range(1, sq + 1):
            if num % i == 0:
                retVal.append(i)
                tmp = num // i
                if tmp != i:
                    retVal.append(tmp)
            if len(retVal) > 4:
                return []
        self.div[num] = retVal.copy()
        return retVal

    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            d = self.divisors(num)
            if len(d) == 4:
                total += sum(d)
        return total


if __name__ == "__main__":
    sol = Solution()
    # nums = [7286, 18704, 70773, 8224, 91675]
    nums = [i for i in range(1, 11)]

    print(sol.sumFourDivisors(nums))
    print("Running Solution...")
