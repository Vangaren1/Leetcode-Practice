from typing import Optional, List
import heapq
from collections import defaultdict, Counter


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        maxSeen = 1
        for idx in range(n):
            frequency = [0] * 26
            for j in range(idx, n):
                frequency[ord(s[j]) - 97] += 1

                target = 0
                valid = True
                for c in frequency:
                    if c:
                        if target == 0:
                            target = c
                        elif c != target:
                            valid = False
                            break
                if valid:
                    maxSeen = max(maxSeen, j - idx + 1)
        return maxSeen


if __name__ == "__main__":
    sol = Solution()
    s = "zzabccy"
    print(sol.longestBalanced(s))
    print("Running Solution...")


"""
#works but times out

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        def check(tmp):
            c = Counter(tmp)
            if len(c.keys()) <= 1:
                return len(tmp)
            if len(set(c.values())) <= 1:
                return len(tmp)
            return -1

        seen = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                seen = max(seen, check(s[i:j]))
        return seen
            
            """
