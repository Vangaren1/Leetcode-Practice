from typing import Optional, List
import heapq
from collections import defaultdict, Counter
from itertools import permutations


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        if len(s) > len(target):
            return ""
        result = ""
        count = defaultdict(int)
        for ch in s:
            count[ch] += 1
        for t in set(target):
            count[t] += 0

        keys = list(count.keys())
        keys.sort()

        tptr = 0

        while tptr < len(target):
            if count.get(target[tptr], 0) > 0:
                result += target[tptr]
                count[target[tptr]] -= 1
            else:
                # find the lexicographically previous character
                currT = target[tptr]
                currIndex = keys.index(currT)

                if currIndex == len(keys) - 1:
                    currIndex -= 1
                    while currIndex >= 0 and count[keys[currIndex]] <= 0:
                        currIndex -= 1
                else:
                    currIndex += 1
                    while currIndex < len(keys) and count[keys[currIndex]] <= 0:
                        currIndex += 1
                    if currIndex == len(keys):
                        currIndex = keys.index(currT) - 1
                        while currIndex >= 0 and count[keys[currIndex]] <= 0:
                            currIndex -= 1
                nextChar = keys[currIndex]
                result += nextChar
                count[nextChar] -= 1
            tptr += 1

        return result


if __name__ == "__main__":
    sol = Solution()
    s = "leet"
    target = "code"
    print(sol.lexGreaterPermutation(s, target))

    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    # t = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # print(sol.lexGreaterPermutation(s, t))
    print("Running Solution...")


""" 
Brute force does work but it's O(n! * n)
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        p = list(permutations(s))

        smallest = None

        for perm in p:
            perm = "".join(perm)
            if perm > target:
                if smallest == None or perm < smallest:
                    smallest = perm

        if smallest is None:
            return ""
        return smallest
"""
