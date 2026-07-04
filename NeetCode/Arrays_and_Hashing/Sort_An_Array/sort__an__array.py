from typing import Optional, List
import heapq
from collections import defaultdict
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeS(array):
            if len(array) <= 1:
                return array
            mid = len(array) // 2
            left = mergeS(array[:mid])
            right = mergeS(array[mid:])
            return merge(left, right)

        def merge(left, right):
            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right)
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        return mergeS(nums)


if __name__ == "__main__":
    sol = Solution()
    nums = [10, 9, 1, 1, 1, 2, 3, 1]
    print(sol.sortArray(nums))
    print("Running Solution...")


""" 
works but fails on leetcode 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def partition(low, high):
            pivot_index = random.randint(low, high)
            swap(pivot_index, high)
            pivot = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] < pivot:
                    i += 1
                    swap(i, j)
            swap(i + 1, high)
            return i + 1

        def quick(low, high):
            if low < high:
                pivot = partition(low, high)
                quick(low, pivot - 1)
                quick(pivot + 1, high)

        quick(0, len(nums) - 1)
        return nums
"""
