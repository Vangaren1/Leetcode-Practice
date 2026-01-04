from typing import Optional, List
from collections import defaultdict


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = defaultdict(int)

        for num in nums:
            c[num] += 1

        longest = 0
        for num in nums:
            if (num + 1) in c:
                longest = max(c[num] + c[num + 1], longest)
        return longest


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    print(sol.findLHS(nums))
    print("Running Solution...")
