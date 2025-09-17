from typing import Optional, List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for index in range(len(nums) - 1, -1, -1):
            for jindex in range(index + 1, len(nums)):
                if nums[index] < nums[jindex]:
                    dp[index] = max(dp[index], 1 + dp[jindex])
        return max(dp)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 4, 3]
    print(sol.lengthOfLIS(nums))
    print("Running Solution...")

# This is too memory heavy
# def lengthOfLIS(self, nums: List[int]) -> int:
#     seq = []

#     for num in nums:
#         check = [n for n in seq if n[-1] < num]
#         if len(check) == 0:
#             seq.append([num])
#             continue
#         for c in check:
#             if num > c[-1] + 1:
#                 seq.append(c.copy())
#             c.append(num)

#     return max([len(s) for s in seq])
