from typing import Optional, List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ptr = 0
        last = float("-inf")

        while ptr < len(nums):
            curr = nums[ptr]
            if curr == 1:
                if (ptr - last) <= k:
                    return False
                last = ptr
            ptr += 1
        return True

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 0, 0, 0, 1, 0, 0, 1]
    k = 2
    print(sol.kLengthApart(nums, k))

    nums = [1, 0, 0, 1, 0, 1]
    k = 2
    print(sol.kLengthApart(nums, k))

    print("Running Solution...")
