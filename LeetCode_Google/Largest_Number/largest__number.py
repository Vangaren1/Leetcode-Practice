from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def mergeSort(arr):
            if len(arr) == 1:
                return arr

            n = len(arr)
            mid = n // 2
            left = mergeSort(arr[:mid])[::-1]
            right = mergeSort(arr[mid:])[::-1]

            result = []

            while left and right:
                if int(left[-1] + right[-1]) > int(right[-1] + left[-1]):
                    result.append(left[-1])
                    left.pop()
                else:
                    result.append(right[-1])
                    right.pop()

            if left:
                result += left[::-1]
            else:
                result += right[::-1]

            return result

        nums = [str(n) for n in nums]

        result = "".join([str(d) for d in mergeSort(nums)])
        return result if result[0] != "0" else "0"

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 30, 34, 5, 9]
    print(sol.largestNumber(nums))
    print("Running Solution...")
