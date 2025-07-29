from typing import Optional, List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        inRange = set(range(1, len(nums) + 1))
        for n in nums:
            if n in inRange:
                inRange.remove(n)
        return list(inRange)


if __name__ == "__main__":
    s = Solution()
    print("Running Solution...")
