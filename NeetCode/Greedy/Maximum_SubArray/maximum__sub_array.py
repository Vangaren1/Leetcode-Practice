from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
