from typing import Optional, List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        endGoal = len(nums) - 1

        for index in range(len(nums) - 2, -1, -1):
            if index + nums[index] >= endGoal:
                endGoal = index

        return endGoal == 0


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 0, 1, 0]
    print(sol.canJump(nums))
    print("Running Solution...")
