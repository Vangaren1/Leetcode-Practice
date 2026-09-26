from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] ^ nums[1]
        nums.sort()
        best = 0
        for num in nums:
            print(bin(num))

        largestBits = []

        blen = nums[-1].bit_length()

        while nums and nums[-1].bit_length() == blen:
            largestBits.append(nums.pop())

        # if nums is empty, that means all teh numbers have the same bitlength
        if len(nums) == 0:
            newList = [((1 << blen - 1) - 1) & num for num in largestBits]
            return self.findMaximumXOR(newList)

        for num in nums:
            for large in largestBits:
                best = max(best, num ^ large)
        print(largestBits)
        print(nums)
        return best


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 6, 7]
    print(sol.findMaximumXOR(nums))
    print("Running Solution...")
