from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for qury in queries:
            for idx in range(qury[0], qury[1] + 1, qury[2]):
                nums[idx] = (nums[idx] * qury[3]) % (10**9 + 7)

        result = nums[0]
        for index in range(1, len(nums)):
            result ^= nums[index]
        return result


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 1, 5, 4]
    queries = [[1, 4, 2, 3], [0, 2, 1, 2]]
    print(sol.xorAfterQueries(nums, queries))
    print("Running Solution...")
