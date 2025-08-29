from typing import Optional, List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(index: int, curr: list, total: int):
            if total == target:
                results.append(curr.copy())
                return

            if total > target or index >= len(nums):
                return

            curr.append(nums[index])
            dfs(index, curr.copy(), total + nums[index])
            curr.pop()
            dfs(index + 1, curr, total)

        dfs(0, [], 0)
        return results


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 5, 6, 9]
    target = 9

    print(sol.combinationSum(nums, target))
    print("Running Solution...")
