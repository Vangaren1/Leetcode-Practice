from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        for left in range(len(nums) - 3):
            for right in range(len(nums) - 1, left + 2, -1):
                l, r = left + 1, right - 1
                while l < r:
                    if l > left + 1 and nums[l] == nums[l - 1]:
                        l += 1
                        continue
                    if r < right - 1 and nums[r] == nums[r + 1]:
                        r -= 1
                        continue
                    tmp = nums[left] + nums[right] + nums[l] + nums[r]
                    if tmp == target:
                        res.add((nums[left], nums[l], nums[r], nums[right]))
                        r -= 1
                        l += 1
                    elif tmp < target:
                        l += 1
                    else:
                        r -= 1

        return [[a, b, c, d] for a, b, c, d in res]


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 3, -3, 1, 0]
    target = 3
    print(sol.fourSum(nums, target))
    print("Running Solution...")
