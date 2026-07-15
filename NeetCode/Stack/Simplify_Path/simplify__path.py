from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stk = []
        for p in paths:
            if p:
                if p == "..":
                    if stk:
                        stk.pop()
                elif p == ".":
                    continue
                else:
                    stk.append(p)
        return "/" + "/".join(stk)


if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath("/neetcode/practice//...///../courses"))
    print(sol.simplifyPath("/..//"))
    print(sol.simplifyPath("/..//_home/a/b/..///"))
    print(sol.simplifyPath("/a/./b/../../c/"))
    print("Running Solution...")
