from typing import Optional, List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:

        def check(idx):
            even = set()
            odd = set()
            mVal = -1

            for index in range(idx, len(nums)):
                num = nums[index]
                if num % 2 == 0:
                    even.add(num)
                else:
                    odd.add(num)

                if len(even) == len(odd):
                    dist = index + 1 - idx
                    mVal = max(dist, mVal)

            return mVal

        result = 0
        for i in range(len(nums)):
            c = check(i)
            result = max(c, result)
        return result

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 2]
    print(sol.longestBalanced(nums))

    print("Running Solution...")
