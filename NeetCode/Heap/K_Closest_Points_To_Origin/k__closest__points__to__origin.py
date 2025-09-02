from typing import Optional, List
import heapq, math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return math.sqrt(x**2 + y**2)

        distList = []
        for point in points:
            d = dist(point[0], point[1])
            heapq.heappush(distList, (-d, point))
            if len(distList) > k:
                heapq.heappop(distList)

        return [i[1] for i in distList]


if __name__ == "__main__":
    sol = Solution()
    points = [[0, 2], [2, 0], [2, 2]]
    k = 2

    print(sol.kClosest(points, k))
    print("Running Solution...")
