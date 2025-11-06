from typing import Optional, List
from collections import defaultdict
import heapq


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def calc(arr):
            h = defaultdict(int)
            for n in arr:
                h[n] += 1
            l = []
            for key, item in h.items():
                heapq.heappush(l, (-item, -key))
            total = 0

            for _ in range(x):
                if l:
                    tmp = heapq.heappop(l)
                    total += -tmp[1] * -tmp[0]
            return total

        ptr1 = 0
        ptr2 = k
        retArr = []

        while ptr2 <= len(nums):
            retArr.append(calc(nums[ptr1:ptr2]))
            ptr1 += 1
            ptr2 += 1
        return retArr

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [9, 2, 2]
    k = 3
    x = 3
    print(sol.findXSum(nums, k, x))
    print("Running Solution...")
