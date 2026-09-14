from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        last = chars[0]
        charCount = 1
        cPtr = 0
        for index in range(1, n):
            curr = chars[index]
            if curr == last:
                charCount += 1
                continue

            chars[cPtr] = last
            cPtr += 1
            if charCount > 1:
                for digit in str(charCount):
                    chars[cPtr] = digit
                    cPtr += 1

            last = curr
            charCount = 1
        chars[cPtr] = last
        cPtr += 1
        if charCount > 1:
            for digit in str(charCount):
                if cPtr < n:
                    chars[cPtr] = digit
                    cPtr += 1
        return cPtr


if __name__ == "__main__":
    sol = Solution()
    chars = [
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "b",
        "c",
        "c",
        "c",
        "c",
        "c",
        "c",
        "c",
        "c",
        "c",
        "c",
        "c",
        "c",
        "c",
        "c",
    ]
    print(sol.compress(chars))

    print(sol.compress(["a", "a", "b", "b", "c", "c", "c"]))

    print("Running Solution...")
