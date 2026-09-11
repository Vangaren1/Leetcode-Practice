from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        curr = 1
        count = 0
        n = len(nums)

        for right in range(n):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1

            count += right - left + 1

        return count


if __name__ == "__main__":
    sol = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    print(sol.numSubarrayProductLessThanK(nums, k))
    print("Running Solution...")


""" 
O(N^2)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0 
        count = 0
        n = len(nums)
        fromLeft = 1
        for index in range(n):
            fromLeft *= nums[index]
            curr = fromLeft            
            for left in range(index+1):
                if curr < k: 
                    count += 1
                else:
                    curr //= nums[left]
        return count 

"""
