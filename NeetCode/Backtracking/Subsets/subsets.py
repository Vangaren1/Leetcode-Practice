from typing import Optional, List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        curr = []

        def dfs(index):
            if index >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[index])
            dfs(index + 1)

            curr.pop()
            dfs(index + 1)

        dfs(0)

        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.subsets([1, 2, 3]))
    print("Running Solution...")
