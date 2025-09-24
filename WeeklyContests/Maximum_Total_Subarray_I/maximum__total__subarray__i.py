from typing import Optional, List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        def arrayVal(left, right):
            highest = max(nums[left : right + 1])
            lowest = min(nums[left : right + 1])
            return highest - lowest

        return k * arrayVal(0, len(nums) - 1)


# this one was a trick.  because you can use the same subarray more than once, you
# just need to find the max and min values of the entire array, and multiple that times k
# because no matter what, any subarray can at BEST return the value of the max and min values for
# the entire array.


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 2]
    k = 2

    print(sol.maxTotalValue(nums, k))
    print("Running Solution...")
