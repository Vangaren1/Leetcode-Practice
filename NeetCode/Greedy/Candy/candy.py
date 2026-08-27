from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1 for _ in range(n)]
        for index in range(1, n):
            if ratings[index] > ratings[index - 1]:
                candies[index] = candies[index - 1] + 1

        for index in range(n - 2, -1, -1):
            if ratings[index] > ratings[index + 1]:
                candies[index] = max(candies[index], candies[index + 1] + 1)

        return sum(candies)


if __name__ == "__main__":
    sol = Solution()
    print(sol.candy([1, 3, 2, 2, 1]))
    print(sol.candy([2, 3, 3]))
    print(sol.candy([1, 0, 2]))
    print("Running Solution...")
