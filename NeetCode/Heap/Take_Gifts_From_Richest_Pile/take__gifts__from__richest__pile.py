from typing import Optional, List
import heapq, math
from collections import defaultdict


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        hq = []

        for gift in gifts:
            heapq.heappush(hq, (-1) * gift)

        for _ in range(k):

            curr = -heapq.heappop(hq)
            curr = math.floor(math.sqrt(curr))
            heapq.heappush(hq, (-1) * curr)

        return -sum(hq)

        pass


if __name__ == "__main__":
    sol = Solution()
    gifts = [25, 64, 9, 4, 100]
    k = 4
    print(sol.pickGifts(gifts, k))
    print("Running Solution...")
