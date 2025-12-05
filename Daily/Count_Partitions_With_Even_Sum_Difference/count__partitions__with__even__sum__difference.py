from typing import Optional, List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        growing = 0
        count = 0
        for index in range(len(nums) - 1):
            num = nums[index]
            growing += num
            totalSum -= num
            if abs(growing - totalSum) % 2 == 0:
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()

    nums = [10, 10, 3, 7, 6]
    print(sol.countPartitions(nums))

    nums = [1, 2, 2]
    print(sol.countPartitions(nums))

    print("Running Solution...")
