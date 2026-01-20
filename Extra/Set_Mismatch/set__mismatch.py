from typing import Optional, List
from collections import defaultdict


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        curr = sum(nums)
        target = (n * (n + 1)) // 2
        c = defaultdict(int)
        for num in nums:
            c[num] += 1
            if c[num] == 2:
                c = num
                break
        return [c, target - (curr - c)]


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 2, 4]
    print(sol.findErrorNums(nums))
    print("Running Solution...")
