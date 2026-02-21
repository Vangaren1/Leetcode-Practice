from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        def check(index):
            stuple = (set(), set())

            s = 0
            for idx in range(index, n):
                num = nums[idx]
                stuple[num % 2].add(num)
                if len(stuple[0]) == len(stuple[1]):
                    s = max(idx - index + 1, s)
            return s

        seen = -1
        for idx in range(n):
            seen = max(seen, check(idx))

        return seen


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 2, 5, 4]
    print(sol.longestBalanced(nums))
    print("Running Solution...")
