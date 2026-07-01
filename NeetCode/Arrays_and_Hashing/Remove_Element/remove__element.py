from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        k = len(nums) - count[val]
        count[val] = 0
        ptr = 0
        for key, val in count.items():
            for i in range(val):
                nums[ptr + i] = key
            ptr += val
        return k


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
