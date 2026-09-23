from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        tmp = nums[:]
        tmp.sort()
        countBelow = {}

        ptr = 0
        prev = None
        while ptr < len(tmp):
            if prev != tmp[ptr]:
                countBelow[tmp[ptr]] = ptr
            prev = tmp[ptr]
            ptr += 1

        return [countBelow[num] for num in nums]
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [8, 1, 2, 2, 3]
    print(sol.smallerNumbersThanCurrent(nums))
    print("Running Solution...")
