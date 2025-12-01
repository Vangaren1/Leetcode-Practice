from typing import Optional, List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        total = 0
        res = []
        for index in range(len(nums)):
            total *= 2
            total += nums[index]
            res.append(total % 5 == 0)
            total %= 5
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0]
    print(sol.prefixesDivBy5(nums))

    print("Running Solution...")
