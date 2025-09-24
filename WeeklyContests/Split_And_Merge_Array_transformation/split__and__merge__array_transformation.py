from typing import Optional, List

from collections import defaultdict, deque


class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        if n == 0:
            return 0

        # 1) For each value, queue the indices where it appears in num2 (left-to-right)
        pos = defaultdict(deque)
        for j, v in enumerate(nums2):
            pos[v].append(j)

        # 2) Map each element in num1 to its next target index in num2 → P
        #    (This respects duplicate occurrences by consuming indices in order.)
        P = [
            pos[v].popleft() for v in nums1
        ]  # valid since num1 is a permutation of num2

        # 3) Longest subsequence with consecutive-by-1 values (x, x+1, x+2, ...)
        #    One-pass DP: best[v] = 1 + best[v-1] as we scan left→right.
        best = {}
        longest = 0
        for x in P:
            best[x] = best.get(x - 1, 0) + 1
            if best[x] > longest:
                longest = best[x]

        # 4) Minimum moves = n - longest kept block
        return n - longest


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 1, 2, 3, 4, 5]
    nums2 = [5, 4, 3, 2, 1, 1]
    print(sol.minSplitMerge(nums1, nums2))

    # nums1 = [3, 1, 2]
    # nums2 = [1, 2, 3]
    # print(sol.minSplitMerge(nums1, nums2))

    print("Running Solution...")
