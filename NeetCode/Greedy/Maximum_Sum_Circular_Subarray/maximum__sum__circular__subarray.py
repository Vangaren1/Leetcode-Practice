from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        bestMax = nums[0]
        bestMin = nums[0]
        total = 0

        for num in nums[1:]:
            total += num
            currMax = max(num, currMax + num)
            bestMax = max(bestMax, currMax)
            currMin = min(num, currMin + num)
            bestMin = min(bestMin, currMin)

        if bestMax < 0:
            return bestMax

        return max(bestMax, total - bestMin)

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
    print(sol.maxSubarraySumCircular([5, -3, 5]))

    nums = [-2, 4, -5, 4, -5, 9, 4]

    nums = [2, 3, -4]
    print("Running Solution...")
