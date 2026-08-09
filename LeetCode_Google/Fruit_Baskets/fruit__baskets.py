from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        maxseen = 0
        count = defaultdict(int)

        for right, fruit in enumerate(fruits):
            count[fruit] += 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]

                left += 1

            maxseen = max(maxseen, right - left + 1)

        return maxseen


if __name__ == "__main__":
    sol = Solution()
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    print(sol.totalFruit(fruits))
    print("Running Solution...")
