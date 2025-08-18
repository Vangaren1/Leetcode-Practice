from typing import Optional, List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == "__main__":
    sol = Solution()

    nums = [-1, 0, 2, 4, 6, 8]
    target = 4
    print(sol.search(nums, target))
    print("Running Solution...")
