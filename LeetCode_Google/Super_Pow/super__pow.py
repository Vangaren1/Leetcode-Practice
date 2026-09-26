from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        result = 1

        for digit in b:
            result = (pow(result, 10, 1337) * pow(a, digit, 1337)) % 1337

        return result


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
