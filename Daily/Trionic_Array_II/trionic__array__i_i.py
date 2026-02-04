from typing import Optional, List

# incomplete


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        updowns = []
        increasing = False

        ptr = 0

        while ptr < len(nums) - 1 and nums[ptr] >= nums[ptr + 1]:
            ptr += 1
        increasing = True
        updowns.append((0, increasing))

        for index in range(ptr, len(nums) - 1):
            if increasing and nums[index] > nums[index + 1]:
                increasing = False
                updowns.append((index, False))
            elif not increasing and nums[index] < nums[index + 1]:
                increasing = True
                updowns.append((index, True))
            elif nums[index] == nums[index + 1]:
                updowns = []

        updowns.append((len(nums) - 1, increasing))

        if not updowns[0][1]:
            updowns.pop(0)

        maxFound = float("-inf")
        ptr = 0
        while ptr < len(updowns) - 3:
            start = updowns[ptr][0]
            end = updowns[ptr + 3][0]
            n = nums[start : end + 1]
            # print(n)
            maxFound = max(maxFound, sum(n))
            ptr += 2
        return maxFound


if __name__ == "__main__":
    sol = Solution()
    # nums = [0, -2, -1, -3, 0, 2, -1]
    nums = [1, 4, 2, 7]
    nums = [1, 4, 2, 2, 3, 1, 2]
    print(sol.maxSumTrionic(nums))
    print("Running Solution...")
