from typing import Optional, List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]

            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = nums = [4, 5, 1, 2, 3]

    print(sol.findMin(nums))
    # print(sol.findMin([3, 4, 5, 1, 2]))
    print("Running Solution...")
