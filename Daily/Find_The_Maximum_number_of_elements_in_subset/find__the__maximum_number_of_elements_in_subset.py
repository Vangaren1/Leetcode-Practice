from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c = defaultdict(int)
        for num in nums:
            c[num] += 1
        count = 0
        for key, value in c.items():
            tmp = 1
            if key in (0, 1):
                tmp = c[key] - (c[key] % 2 + 1) * 1
            else:
                k, v = key, value
                while v >= 2 and k * k in c:
                    k = k * k
                    v = c[k]
                    tmp += 2
            count = max(count, tmp)
        return count

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 5, 1, 2, 2]
    print(sol.maximumLength(nums))
    print("Running Solution...")
