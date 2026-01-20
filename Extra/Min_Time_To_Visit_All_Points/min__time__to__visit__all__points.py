from typing import Optional, List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def minTime(a, b):
            x1, y1 = a
            x2, y2 = b
            dy = abs(y2 - y1)
            dx = abs(x2 - x1)
            if dx == 0:
                return dy
            if dy == 0:
                return dx
            if dy < dx:
                return dy + (dx - dy)
            else:
                return dx + (dy - dx)

        total = 0
        ptr = 0
        while ptr < len(points) - 1:
            total += minTime(points[ptr], points[ptr + 1])
            ptr += 1
        return total


if __name__ == "__main__":
    sol = Solution()
    points = [[1, 1], [3, 4], [-1, 0]]
    expected = 7

    print(sol.minTimeToVisitAllPoints(points))
    print("Running Solution...")
