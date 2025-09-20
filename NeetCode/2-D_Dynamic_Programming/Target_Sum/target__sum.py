from typing import Optional, List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in cache:
                return cache[(index, total)]

            curr = nums[index]
            cache[(index, total)] = dfs(index + 1, total - curr) + dfs(
                index + 1, total + curr
            )
            return cache[(index, total)]

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 2]
    target = 6
    print(sol.findTargetSumWays(nums, target))
    print("Running Solution...")
