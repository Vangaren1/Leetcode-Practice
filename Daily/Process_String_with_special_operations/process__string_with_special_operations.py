from typing import Optional, List
import heapq
from collections import defaultdict

"""
If the letter is a lowercase English letter append it to result.
A '*' removes the last character from result, if it exists.
A '#' duplicates the current result and appends it to itself.
A '%' reverses the current result.
"""
import string


class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for ch in s:
            if ch in string.ascii_lowercase:
                result += ch
            elif ch == "*":
                result = result[:-1]
            elif ch == "#":
                result += result
            elif ch == "%":
                result = result[::-1]
        return result


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
