from typing import Optional, List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            index = nums.index(original)
            nums.pop(index)
            original *= 2

        return original


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 3, 6, 1, 12]
    original = 3
    print(sol.findFinalValue(nums, original))
    print("Running Solution...")
