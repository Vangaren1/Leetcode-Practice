from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        mid = left + (right - left) // 2
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        while left < right:
            mid = left + (right - left) // 2
            # check if mid is even or odd
            even = mid % 2 == 0

            # if even, and the number to the right is the same, the unqiue number is to the right
            if even and mid < len(nums) - 1:
                if nums[mid] == nums[mid + 1]:
                    left = mid
                    continue
                else:
                    # if the number to the right is not hte same, check to the left, otherwise its to the right
                    if nums[mid] != nums[mid - 1]:
                        return nums[mid]
                    right = mid
                    continue
            elif not even and mid < len(nums) - 1:
                # if odd and the numbers match the number is to the left
                if nums[mid] == nums[mid + 1]:
                    right = mid
                    continue
                else:
                    if nums[mid] != nums[mid - 1]:
                        return nums[mid]
                    left = mid

        return -1

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 3, 7, 7, 10, 11, 11]
    digi = [0, 1, 2, 3, 4, 5, 6]
    print(sol.singleNonDuplicate(nums))
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    digi = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(sol.singleNonDuplicate(nums))
    print("Running Solution...")
