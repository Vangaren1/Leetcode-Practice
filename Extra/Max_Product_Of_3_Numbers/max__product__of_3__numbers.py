from typing import Optional, List
import heapq


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 3:
            return nums[0] * nums[1] * nums[2]

        nums.sort()

        big3 = nums[-1] * nums[-2] * nums[-3]
        small3 = nums[0] * nums[1] * nums[2]

        mid1 = nums[0] * nums[1] * nums[-1]

        return max(big3, small3, mid1)


if __name__ == "__main__":
    sol = Solution()

    print(sol.maximumProduct([1, 2, 3]))
    print(sol.maximumProduct([1, 2, 3, 4]))
    print(sol.maximumProduct([-1, -2, -3]))
    print(sol.maximumProduct([-100, -98, -1, 2, 3, 4]))
    print(sol.maximumProduct([-100, -2, -3, 1]))
    print("Running Solution...")
