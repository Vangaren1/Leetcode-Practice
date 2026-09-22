from typing import Optional, List
import heapq
from collections import defaultdict, Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = defaultdict(int)
        for num in arr:
            c[num] += 1

        hq = []
        for key, val in c.items():
            heapq.heappush(hq, (val, key))

        while k and hq:
            count, val = heapq.heappop(hq)
            if count <= k:
                del c[val]
                k -= count
            else:
                break
        return len(c)


if __name__ == "__main__":
    sol = Solution()
    arr = [5, 5, 4]
    k = 1
    print(sol.findLeastNumOfUniqueInts(arr, k))
    print("Running Solution...")
