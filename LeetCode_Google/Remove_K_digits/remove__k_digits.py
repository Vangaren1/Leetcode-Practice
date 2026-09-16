from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"

        stk = []

        for index in range(len(num)):
            d = num[index]

            while stk and stk[-1] > d and k > 0:
                k -= 1
                stk.pop()
            stk.append(d)

        while stk and k:
            k -= 1
            stk.pop()

        if len(stk) == 0:
            return "0"

        result = "".join(stk)
        while len(result) > 1 and result[0] == "0":
            result = result[1:]
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeKdigits("10", 1))
    print("Running Solution...")


""" 

works, but is O(N^2)
 
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        def removeOne(n):
            for i in range(len(n) - 1):
                if n[i] > n[i + 1]:
                    return n[:i] + n[i + 1 :]
            return n[:-1]

        for _ in range(k):
            num = removeOne(num)
            if len(num) == 0:
                return "0"

        while num[0] == "0" and len(num) > 1:
            num = num[1:]
        return num
"""
