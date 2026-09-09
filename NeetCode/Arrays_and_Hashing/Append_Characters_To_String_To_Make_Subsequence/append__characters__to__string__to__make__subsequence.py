from typing import Optional, List
import heapq
from collections import defaultdict, Counter


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0

        tPtr = 0

        for ch in s:
            if tPtr < len(t) and t[tPtr] == ch:
                tPtr += 1

        return len(t) - tPtr


if __name__ == "__main__":
    sol = Solution()

    s = "coaching"
    t = "coding"
    print(sol.appendCharacters(s, t))
    print("Running Solution...")


""" 
Fails on s = 'aabb' t = 'abbb'


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0

        sCount = Counter(s)
        tCount = Counter(t)

        tPtr = 0

        # move a pointer forward to see if there
        # is a matching prefix between s and t
        while s[tPtr] == t[tPtr]:
            tCount[t[tPtr]] -= 1
            sCount[t[tPtr]] -= 1
            if tCount[t[tPtr]] <= 0:
                del tCount[t[tPtr]]
            if sCount[t[tPtr]] <= 0:
                del sCount[t[tPtr]]
            tPtr += 1

        total = 0
        # if the next character of t is not in s, you need to add all the remaining characters of t
        sPtr = tPtr
        for tPointer in range(tPtr, len(t)):
            if t[tPointer] not in sCount:
                return len(t) - tPointer

            while sPtr < len(s) and tPtr < len(t) and s[sPtr] != t[tPtr]:
                sCount[s[sPtr]] -= 1
                if sCount[s[sPtr]] <= 0:
                    del sCount[s[sPtr]]
                sPtr += 1

        return 0
"""
