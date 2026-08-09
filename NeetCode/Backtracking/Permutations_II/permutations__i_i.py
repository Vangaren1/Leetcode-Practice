from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        used = [False] * len(nums)

        def dfs(curr: List[int]) -> None:
            if len(curr) == len(nums):
                results.append(curr.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Only use the first unused copy of a duplicate value.
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                curr.append(nums[i])

                dfs(curr)

                curr.pop()
                used[i] = False

        dfs([])
        return results


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2]
    print(sol.permuteUnique(nums))
    print("Running Solution...")


""" 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = set()
        n = len(nums)

        if n == 1:
            return [nums]

        for index in range(n):

            arr = nums.copy()
            tmp = arr.pop(index)

            permutations = self.permuteUnique(arr)

            for perm in permutations:
                t = [tmp] + perm
                results.add(tuple(t))

        return [[i for i in perm] for perm in results]

"""
