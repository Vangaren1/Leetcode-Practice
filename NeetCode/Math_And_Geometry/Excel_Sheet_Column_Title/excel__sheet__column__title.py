from typing import Optional, List
import heapq
from collections import defaultdict
import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = string.ascii_uppercase

        result = ""

        while columnNumber:
            columnNumber -= 1
            let = columnNumber % 26
            result += letters[let]
            columnNumber -= let
            columnNumber //= 26

        return result[::-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.convertToTitle(28))
    print("Running Solution...")
