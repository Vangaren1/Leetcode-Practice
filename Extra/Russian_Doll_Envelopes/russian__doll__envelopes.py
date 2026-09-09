from typing import Optional, List
import heapq
from collections import defaultdict

import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        tails = []
        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        envel = [x[1] for x in envelopes]

        return self.lengthOfLIS(envel)

        pass


if __name__ == "__main__":
    sol = Solution()
    envelopes = [[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]]
    print(sol.maxEnvelopes(envelopes))
    print("Running Solution...")
