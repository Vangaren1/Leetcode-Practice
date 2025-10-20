from typing import Optional, List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:

        mValForward = 0
        even, odd = set(), set()
        for index in range(len(nums)):
            curr = nums[index]
            if curr % 2 == 0:
                even.add(curr)
            else:
                odd.add(curr)

            if len(even) == len(odd):
                mValForward = max(index + 1, mValForward)

        mValBack = 0
        even, odd = set(), set()
        for index in range(len(nums) - 1, -1, -1):
            curr = nums[index]
            if curr % 2 == 0:
                even.add(curr)
            else:
                odd.add(curr)

            if len(even) == len(odd):
                mValBack = max(len(nums) - index, mValBack)

        # print(evenOddCountForward)
        # print(evenOddCountBackwards)

        return max(mValForward, mValBack)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 2]
    print(sol.longestBalanced(nums))

    print("Running Solution...")
