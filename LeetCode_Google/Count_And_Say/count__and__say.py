from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.rle(self.countAndSay(n - 1))

    def rle(self, s: str) -> str:
        result = ""

        count = 1
        last = s[0]
        for index in range(1, len(s)):
            ch = s[index]
            if ch == last:
                count += 1
                continue
            result += str(count) + last
            last = ch
            count = 1
        result += str(count) + last
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(4))
    print("Running Solution...")
