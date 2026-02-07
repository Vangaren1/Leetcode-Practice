from typing import Optional, List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        arr = []

        n = len(nums)
        ptr1, ptr2 = 0, n - 1
        while ptr1 < ptr2:
            arr.append(nums[ptr1] + nums[ptr2])
            ptr1 += 1
            ptr2 -= 1
        return max(arr)

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 5, 4, 2, 4, 6]
    print(sol.minPairSum(nums))
    print("Running Solution...")
