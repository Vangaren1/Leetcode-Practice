from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boatCount = 0
        people.sort()

        left, right = 0, len(people) - 1
        while left <= right:

            if people[left] + people[right] <= limit:

                left += 1
            right -= 1
            boatCount += 1
        return boatCount
        pass


if __name__ == "__main__":
    sol = Solution()
    people = [1, 3, 2, 3, 2]
    limit = 3
    print(sol.numRescueBoats(people, limit))
    people = [5, 1, 4, 2]
    limit = 6
    print(sol.numRescueBoats(people, limit))
    print("Running Solution...")
