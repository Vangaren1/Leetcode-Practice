from typing import Optional, List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        s = 0

        for index in range(0, n, 2):
            s += min(nums[index], nums[index + 1])
        return s


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 4, 3, 2]
    assert sol.arrayPairSum(nums) == 4

    nums = [6, 2, 6, 5, 1, 2]
    assert sol.arrayPairSum(nums) == 9
    print("Running Solution...")
