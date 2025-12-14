from typing import Optional, List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        if n <= 2:
            return 0

        pass


if __name__ == "__main__":
    sol = Solution()
    n = 5
    buildings = [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]

    print(sol.countCoveredBuildings(n, buildings))
    print("Running Solution...")
