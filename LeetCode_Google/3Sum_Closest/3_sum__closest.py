from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        currBest = nums[0] + nums[1] + nums[2]

        for index in range(len(nums) - 2):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                check = nums[left] + nums[index] + nums[right]
                if abs(target - check) < abs(target - currBest):
                    currBest = check
                if check < target:
                    left += 1
                elif check > target:
                    right -= 1
                else:
                    return target

        return currBest


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 0]
    target = 100
    print(sol.threeSumClosest(nums, target))
    print("Running Solution...")
