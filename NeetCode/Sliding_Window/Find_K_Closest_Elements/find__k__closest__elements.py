from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = left + (right - left) // 2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k]


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 5, 8]
    k = 2
    x = 6
    print(sol.findClosestElements(arr, k, x))
    print("Running Solution...")
