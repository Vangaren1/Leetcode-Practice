from typing import Optional, List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        ptr = 0
        count = 0
        while ptr < len(nums) - 2:

            if nums[ptr] == nums[ptr + 1] == nums[ptr + 2]:
                nums.pop(ptr)
                count += 1
            else:
                ptr += 1

        while count > 0:
            nums.append(0)
            count -= 1

        return len(nums)


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(sol.removeDuplicates(nums))
    print(nums)
    print("Running Solution...")
