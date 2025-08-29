from typing import Optional, List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        nums = [i for i in range(1, n + 1)]

        def dfs(index, curr):
            if len(curr) == k:
                results.append(curr)
                return

            if index >= len(nums):
                return

            curr.append(nums[index])
            dfs(index + 1, curr.copy())
            curr.pop()
            dfs(index + 1, curr.copy())

        dfs(0, [])

        return results


if __name__ == "__main__":
    sol = Solution()
    print(sol.combine(4, 2))
    print("Running Solution...")
