from typing import Optional, List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        def find(target):

            for i in range(1, target):
                iPlus = i + 1
                bitOr = i | iPlus
                if bitOr == target:
                    return i
            return -1

        for index in range(n):
            ans.append(find(nums[index]))

        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 5, 7]
    print(sol.minBitwiseArray(nums))
    print("Running Solution...")
