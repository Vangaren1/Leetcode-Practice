from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxArr = [nums[0]]
        minArr = [nums[-1]]

        for index in range(1, len(nums)):
            if nums[index] > maxArr[-1]:
                maxArr.append(nums[index])
            else:
                maxArr.append(maxArr[-1])

        for index in range(len(nums) - 2, -1, -1):
            if nums[index] < minArr[-1]:
                minArr.append(nums[index])
            else:
                minArr.append(minArr[-1])
        minArr = minArr[::-1]
        for index in range(len(nums)):
            score = maxArr[index] - minArr[index]
            if score <= k:
                return index
        return -1

        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstStableIndex([5, 0, 1, 4], 3))

    print("Running Solution...")
