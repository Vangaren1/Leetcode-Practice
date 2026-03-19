from typing import Optional, List
import heapq
from collections import defaultdict
import string


class Solution:
    def decodeString(self, s: str) -> str:
        if "[" not in s:
            return s

        nstart = 0
        while not s[nstart].isdigit():
            nstart += 1

        left = nstart
        while not s[left].isdigit():
            left += 1

        # find the first bracket
        start = 0
        while s[start] != "[":
            start += 1

        # n is the number of times to to multiple the []
        n = int(s[left:start])

        # find the matching ']'

        ptr = start + 1
        count = 1
        while count > 0:
            if s[ptr] == "[":
                count += 1
            elif s[ptr] == "]":
                count -= 1
            ptr += 1

        front = s[0:nstart]
        tmp = s[start + 1 : ptr - 1]
        mid = self.decodeString(tmp)
        end = self.decodeString(s[ptr:])

        return front + n * mid + end


if __name__ == "__main__":
    sol = Solution()

    s = "100[leetcode]"
    print(sol.decodeString(s))

    s = "3[a]2[bc]"
    print(sol.decodeString(s))

    s = "3[a2[c]]"
    print(sol.decodeString(s))

    print("Running Solution...")
