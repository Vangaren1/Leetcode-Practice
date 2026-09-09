from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        n = len(s)
        numSet = set(range(len(s)))
        for index, ch in enumerate(s):
            if ch == "(":
                stk.append(index)
            else:
                if stk:
                    idx = stk.pop()
                    numSet.remove(index)
                    numSet.remove(idx)
                # print(f"index: {index}, {idx}")

        print(numSet)

        maxSeen = 0
        curr = 0

        for num in range(n):
            if num in numSet:
                curr = 0
            else:
                curr += 1
                maxSeen = max(maxSeen, curr)
        return maxSeen

        pass


if __name__ == "__main__":
    sol = Solution()
    s = "()((())"
    print(sol.longestValidParentheses(s))
    s = "()(())"
    print(sol.longestValidParentheses(s))
    s = "(((("
    print(sol.longestValidParentheses(s))
    s = ")((()))()()"
    print(sol.longestValidParentheses(s))
    print("Running Solution...")
