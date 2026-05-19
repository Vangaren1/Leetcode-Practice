from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ptr1, ptr2 = 0, 0
        while nums1[ptr1] != nums2[ptr2]:
            if nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1

            else:
                ptr2 += 1
        return nums1[ptr1]


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 3, 6]
    nums2 = [2, 3, 4, 5]
    print(sol.getCommon(nums1, nums2))
    print("Running Solution...")
