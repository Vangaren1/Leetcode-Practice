from typing import Optional, List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        nums.sort()

        for index in range(1, len(nums)):
            left = 0
            right = len(nums) - 1
            while left < index and right > index:
                check = nums[left] + nums[index] + nums[right]
                if check == 0:
                    res.add((nums[left], nums[index], nums[right]))
                if check < 0:
                    left += 1
                else:
                    right -= 1

        return [list(p) for p in res]

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 0, -2, -1, 1, 2]
    print(sol.threeSum(nums))
    print("Running Solution...")
