from typing import Optional, List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for index in range(len(nums)):
            if nums[abs(nums[index]) - 1] < 0:
                return abs(nums[index])
            nums[abs(nums[index]) - 1] *= -1

        return 0


if __name__ == "__main__":
    sol = Solution()
    nums = [[3, 1, 3, 4, 2], [1, 2, 3, 4, 4], [1, 2, 3, 2, 2], [1, 3, 4, 2, 2]]
    expected = [3, 4, 2, 2]

    for index, num in enumerate(nums):
        res = sol.findDuplicate(num)
        assert res == expected[index]

    # print(sol.findDuplicate(nums))
    print("Running Solution...")
