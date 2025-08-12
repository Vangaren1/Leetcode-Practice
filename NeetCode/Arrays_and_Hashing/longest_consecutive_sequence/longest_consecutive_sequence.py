from typing import Optional, List

import heapq


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        hq = []
        for n in nums:
            if n not in numSet:
                numSet.add(n)
                heapq.heappush(hq, n)

        count = 0
        mCount = -1
        while hq:
            tmp = heapq.heappop(hq)
            numSet.remove(tmp)
            count = 1
            while (tmp + 1) in numSet:
                tmp = heapq.heappop(hq)
                numSet.remove(tmp)
                count += 1
            mCount = max(mCount, count)

        # print(hq)
        return mCount


if __name__ == "__main__":
    sol = Solution()

    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(sol.longestConsecutive(nums))
    print("Running Solution...")
