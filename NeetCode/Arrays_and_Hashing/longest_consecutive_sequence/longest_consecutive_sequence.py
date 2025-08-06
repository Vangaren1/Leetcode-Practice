from typing import Optional, List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()

        for n in nums:
            numSet.add(n)

        count = 0

        for n in list(numSet):
            tmp = n
            thiscount = 1
            while True:
                if (tmp + 1) in numSet:
                    tmp = tmp + 1
                    thiscount += 1
                else:
                    break
            count = max(count, thiscount)

        return count


if __name__ == "__main__":
    sol = Solution()

    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(sol.longestConsecutive(nums))
    print("Running Solution...")
