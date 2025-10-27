from typing import Optional, List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        kth = []

        for row in matrix:
            for num in row:
                heapq.heappush(kth, -num)
                if len(kth) > k:
                    heapq.heappop(kth)
        return -kth[0]

        pass


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15],
    ]
    k = 8
    print(sol.kthSmallest(matrix, k))
    print("Running Solution...")
