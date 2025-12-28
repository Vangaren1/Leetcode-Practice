from typing import Optional, List


class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        dp = []
        n = len(nums)

        pre = float("inf")
        for index in range(n - 1, -1, -1):
            pre = min(nums[index], pre)
            dp.append(pre)

        dp = dp[::-1]

        dp.append(0)
        mScore = float("-inf")
        currSum = 0
        for index in range(n - 1):
            currSum += nums[index]
            tmp = currSum - dp[index + 1]
            mScore = max(tmp, mScore)

        return mScore


if __name__ == "__main__":
    sol = Solution()
    nums = [-7, -5, 3]
    assert sol.maximumScore(nums) == -2

    assert sol.maximumScore([10, -1, 3, -4, -5]) == 17

    assert sol.maximumScore([1, 1]) == 0

    print("Running Solution...")
