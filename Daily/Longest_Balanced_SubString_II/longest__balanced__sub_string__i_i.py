from typing import Optional, List
import heapq
from collections import defaultdict, Counter


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        count = Counter(s)

        if len(count.keys()) == 1:
            return n

        c = defaultdict(int)
        maxSeen = 1

        if len(count.keys()) == 2:
            k1, k2 = count.keys()
            hMap = {0: 0}

            for idx in range(n):
                c[s[idx]] += 1
                dx = c[k1] - c[k2]
                if dx in hMap:
                    tmp = idx - hMap[dx] + 1
                    maxSeen = max(maxSeen, tmp)
                else:
                    hMap[dx] = idx + 1
            return maxSeen

        hMap = {(0, 0): 0}
        dxMap = {0: 0}
        c["a"], c["b"], c["c"] = 0, 0, 0

        for idx in range(n):
            c[s[idx]] += 1
            zCount = sum([1 if v == 0 else 0 for v in c.values()])
            # if zCount == 2, then there's only 1 character so far, report the lenght as max
            if zCount == 2:
                maxSeen = max(maxSeen, idx + 1)

            # if zCount == 1 then there's 1 pair of characters so far, need to find that longest
            # so use dx to determine which column to store in dxMap
            tu = (c["b"] - c["a"], c["c"] - c["a"])
            pref = idx + 1
            if zCount == 1:
                dx = 0 if c["c"] == 0 else 1
                if tu[dx] in dxMap:
                    tmp = pref - dxMap[tu[dx]]
                    maxSeen = max(maxSeen, tmp)
                else:
                    dxMap[tu[dx]] = idx

            # here we check the max length considering all 3 chars
            if tu in hMap:
                tmp = pref - hMap[tu]
                maxSeen = max(maxSeen, tmp)
            else:
                hMap[tu] = pref
        return maxSeen


if __name__ == "__main__":
    sol = Solution()
    s = "abbac"
    print(sol.longestBalanced(s))
    print("Running Solution...")
