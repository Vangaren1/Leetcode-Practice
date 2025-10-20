from typing import Optional, List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        mul = 1

        while mul * k in nums:
            mul += 1
        return mul * k
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [8, 2, 3, 4, 6]
    k = 2

    print(sol.missingMultiple(nums, k))
    print("Running Solution...")
