from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1, arr2 = [nums[0]], [nums[1]]

        for index in range(2, n):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[index])
            else:
                arr2.append(nums[index])
        return arr1 + arr2

        pass


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
