from typing import Optional, List
import heapq
from collections import defaultdict, Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        if max(count.values()) > (len(s) + 1) // 2:
            return ""

        minArray = []

        for key, val in count.items():
            heapq.heappush(minArray, [-val, key])

        result = ""
        prev = None

        while minArray:

            val, key = heapq.heappop(minArray)

            result += key
            val += 1

            if prev:
                heapq.heappush(minArray, prev)

            if val < 0:
                prev = [val, key]
            else:
                prev = None

        return result

        return

        pass


if __name__ == "__main__":
    sol = Solution()
    s = "abbccdd"
    print(sol.reorganizeString(s))
    print("Running Solution...")
