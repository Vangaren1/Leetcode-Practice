from typing import Optional, List
import heapq, string
from collections import defaultdict


class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        def pattern(s):
            result = [0] * len(s)
            for index in range(1, len(s)):
                result[index] = (ord(s[index]) - ord(s[index - 1])) % 26
            return tuple(result)

        groups = defaultdict(list)

        for w in strings:
            groups[pattern(w)].append(w)

        return [val for val in groups.values()]

        pass


if __name__ == "__main__":
    sol = Solution()
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    print(sol.groupStrings(strings))
    print("Running Solution...")
