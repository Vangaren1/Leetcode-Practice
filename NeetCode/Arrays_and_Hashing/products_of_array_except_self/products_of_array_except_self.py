from typing import Optional, List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [
            1,
        ] * len(nums)
        right = left[:]
        left[0] = 1
        right[-1] = 1

        for index in range(1, len(nums)):
            left[index] = left[index - 1] * nums[index - 1]
        for index in range(len(nums) - 2, -1, -1):
            right[index] = right[index + 1] * nums[index + 1]

        return [left[index] * right[index] for index in range(len(nums))]


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 4, 6]
    print(sol.productExceptSelf(nums))
    print("Running Solution...")
