from typing import Optional, List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        ptr = 0
        switches = 2
        rising = True
        if nums[0] > nums[1]:
            return False
        while ptr < n - 1:
            if nums[ptr] == nums[ptr + 1]:
                return False

            elif nums[ptr] > nums[ptr + 1] and rising:
                switches -= 1
                rising = False

            elif nums[ptr] < nums[ptr + 1] and not rising:
                switches -= 1
                rising = True

            ptr += 1

        return switches == 0


if __name__ == "__main__":
    sol = Solution()

    nums = [8, 9, 4, 6, 1]
    print(sol.isTrionic(nums))
    print("Running Solution...")
