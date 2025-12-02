from typing import Optional, List
from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)

        lastIndex, firstIndex = {}, {}
        for index in range(n):
            first = s[index]
            last = s[-(index + 1)]
            if first not in firstIndex:
                firstIndex[first] = index
            if last not in lastIndex:
                lastIndex[last] = n - index - 1

        total = 0
        for key in firstIndex.keys():
            left = firstIndex[key]
            right = lastIndex[key]

            if (right - left) >= 2:
                total += len(set(s[left + 1 : right]))
        return total


if __name__ == "__main__":
    sol = Solution()
    s = "bbcbaba"
    print(sol.countPalindromicSubsequence(s))
    print("Running Solution...")


"""_summary_
This only works if you can rearrange hte order of the string and just count hte characters.


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = defaultdict(int)

        for ch in s:
            count[ch] += 1

        threeCount, twoCount, oneCount = 0, 0, 0

        for value in count.values():
            if value >= 3:
                threeCount += 1
            if value >= 2:
                twoCount += 1
            if value >= 1:
                oneCount += 1

        return threeCount + twoCount * (oneCount - 1)
        
        
This version had good intiution, using prefix and suffix arrays, 
but examples like s = 'xyxy' wouldn't work here.          
        
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        fStart = [0] * n
        fEnd = [0] * n

        startSet, endSet = set(), set()
        lastIndex, firstIndex = {}, {}
        for index in range(n):
            first = s[index]
            last = s[-(index + 1)]
            if first not in firstIndex:
                firstIndex[first] = index
            if last not in lastIndex:
                lastIndex[last] = n - index - 1
            startSet.add(first)
            endSet.add(last)
            fStart[index] = len(startSet)
            fEnd[-(index + 1)] = len(endSet)

        print(firstIndex)
        print(lastIndex)
        print(fStart)
        print(fEnd)
        """
