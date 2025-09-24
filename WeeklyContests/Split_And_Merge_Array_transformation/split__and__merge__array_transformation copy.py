from typing import Optional, List


class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1 == nums2:
            return 0

        dp = {}

        # left = left part of sub array of nums1
        # right = right part of sub array of nums1
        # index = start of subarray for nums2
        def recursive(left, right, index):
            if (left, right, index) in dp:
                return dp[(left, right, index)]

            if index >= len(nums2):
                dp[(left, right, index)] = 1
                return 1
            if right >= len(nums1):
                dp[(left, right, index)] = 0
                return 0

            diff = right - left
            right2 = index + diff

            first = nums1[left : right + 1]
            second = nums2[index : right2 + 1]
            if first == second:
                dp[(left, right, index)] = recursive(
                    left + diff + 1, right + diff + 1, index + diff + 1
                )
                return dp[(left, right, index)]

            # swap = 1 + recursive(left + 1, right + 1, index + 1)
            increase = 1 + recursive(left, right + 1, index)
            noSwap = 1 + recursive(left + 1, right + 1, index)

            dp[(left, right, index)] = min(noSwap, increase)
            return dp[(left, right, index)]

        return recursive(0, 0, 0)


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 1, 2, 3, 4, 5]
    nums2 = [5, 4, 3, 2, 1, 1]
    print(sol.minSplitMerge(nums1, nums2))

    # nums1 = [3, 1, 2]
    # nums2 = [1, 2, 3]
    # print(sol.minSplitMerge(nums1, nums2))

    print("Running Solution...")
