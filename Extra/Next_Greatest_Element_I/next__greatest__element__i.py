from typing import Optional, List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)

        results = []

        for num in nums1:
            index = nums2.index(num)
            ptr = index + 1
            while ptr < n and nums2[ptr] < num:
                ptr += 1
            if ptr == n:
                results.append(-1)
            else:
                results.append(nums2[ptr])
        return results


if __name__ == "__main__":
    sol = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(sol.nextGreaterElement(nums1, nums2))
    print("Running Solution...")
