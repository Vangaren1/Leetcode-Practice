from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])

        hq = []

        for passenger, origin, destination in trips:
            while hq and hq[0][0] < origin:
                _, p = heapq.heappop(hq)
                capacity += p
            capacity -= passenger
            if capacity < 0:
                return False
            heapq.heappush(hq, (destination, passenger))
        return True

        pass


if __name__ == "__main__":
    sol = Solution()
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4
    print("Running Solution...")


""" 
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hq = []

        for passenger, origin, destination in trips:
            if passenger > capacity:
                return False
            heapq.heappush(hq, (origin, passenger))
            heapq.heappush(hq, (destination, -passenger))

        curr = 0

        while hq:
            _, passenger = heapq.heappop(hq)
            curr += passenger
            if curr > capacity:
                return False

        return True
"""
