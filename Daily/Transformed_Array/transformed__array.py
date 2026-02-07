from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = [None] * n

        for index, num in enumerate(nums):
            if num > 0:
                tmp = (num + index) % n
            else:
                tmp = index - abs(num) % n
            results[index] = nums[tmp]
        return results


if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 4, -1]
    print(sol.constructTransformedArray(nums))
    print("Running Solution...")
