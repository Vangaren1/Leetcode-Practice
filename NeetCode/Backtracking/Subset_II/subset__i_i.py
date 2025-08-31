from typing import Optional, List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()

        def dfs(index):
            if index >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[index])
            dfs(index + 1)

            while (index + 1) < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            curr.pop()
            dfs(index + 1)

        dfs(0)

        return res

    pass


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 1]
    # ?Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]

    print(sol.subsetsWithDup(nums))

    print("Running Solution...")
