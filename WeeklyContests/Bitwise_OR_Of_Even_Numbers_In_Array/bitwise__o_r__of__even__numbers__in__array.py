from typing import Optional, List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        total = 0

        for n in nums:
            if n % 2 == 0:
                total = total | n
        return total


if __name__ == "__main__":
    sol = Solution()
    nums = list(range(7))
    print(sol.evenNumberBitwiseORs(nums))
    print("Running Solution...")
