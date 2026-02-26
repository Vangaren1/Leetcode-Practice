from typing import Optional, List

import heapq


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for num in s:
            if num - 1 not in s:
                y = num
                while y in s:
                    y += 1
                best = max(best, y - num)
        return best


if __name__ == "__main__":
    sol = Solution()

    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(sol.longestConsecutive(nums))
    print("Running Solution...")
