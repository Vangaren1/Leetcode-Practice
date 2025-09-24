from typing import Optional, List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total = total ^ num
        return total


if __name__ == "__main__":
    sol = Solution()
    nums = [7, 6, 6, 7, 8]
    print(sol.singleNumber(nums))
    print("Running Solution...")
