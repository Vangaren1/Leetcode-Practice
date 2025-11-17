from typing import Optional, List


class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums) - 1
        dp = [float("inf")] * (length + 1)
        dp[length] = 0

        for index in range(length - 1, -1, -1):
            for j in range(1, nums[index] + 1):
                if index + j <= length:
                    curr = dp[index]
                    future = 1 + dp[index + j]
                    dp[index] = min(curr, future)

        return dp[0]


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.jump(nums))
    print("Running Solution...")
