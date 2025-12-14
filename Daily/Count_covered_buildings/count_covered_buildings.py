from typing import Optional, List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        if n <= 2:
            return 0
        rows = [[] for _ in range(n)]
        cols = [[] for _ in range(n)]

        for build in buildings:
            y, x = build
            tmp = (y - 1, x - 1)
            rows[y - 1].append(tmp)
            cols[x - 1].append(tmp)

        for col in cols:
            col.sort(key=lambda x: x[0])

        possible = []
        for row in rows:
            if len(row) > 2:
                row.sort(key=lambda x: x[1])
                for index in range(1, len(row) - 1):
                    possible.append(row[index])

        count = 0

        for poss in possible:
            y, x = poss
            colMin = cols[x][0][0]
            colMax = cols[x][-1][0]
            rowMin = rows[y][0][1]
            rowMax = rows[y][-1][1]
            if colMin < y < colMax and rowMin < x < rowMax:
                count += 1

        return count

        pass


if __name__ == "__main__":
    sol = Solution()
    n = 5
    buildings = [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]

    print(sol.countCoveredBuildings(n, buildings))
    print("Running Solution...")
