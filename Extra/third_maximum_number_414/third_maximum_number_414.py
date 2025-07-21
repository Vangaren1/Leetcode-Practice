from typing import Optional, List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        seen = set()

        ptr = 0
        length = len(nums)
        while ptr < length:
            if nums[ptr] in seen:
                nums.pop(ptr)
                length = len(nums)
            else:
                seen.add(nums[ptr])
                ptr += 1
        nums.sort(reverse=True)
        if len(nums) < 3:
            return nums[0]
        return nums[2]


if __name__ == "__main__":
    s = Solution()

    nums = [2, 2, 3, 1]

    print(s.thirdMax(nums))
    print("Running Solution...")
