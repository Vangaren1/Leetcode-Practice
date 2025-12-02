from typing import Optional, List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [nums[0]]

        for index in range(1, n):
            prefix.append(prefix[-1] + nums[index])
        prefix.insert(0, 0)

        valLengths = [i for i in range(1, n + 1) if i % k == 0]

        top = float("-inf")

        for lengths in valLengths:
            i = 0
            while i + lengths <= n:
                j = i + lengths
                curr = prefix[j] - prefix[i]
                top = max(top, curr)

                i += 1
        return top


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2]
    k = 1

    print(sol.maxSubarraySum(nums, k))

    nums = [-1, -2, -3, -4, -5]
    k = 4
    print(sol.maxSubarraySum(nums, k))

    nums = [-5, 1, 2, -3, 4]
    k = 2
    print(sol.maxSubarraySum(nums, k))
    print("Running Solution...")
