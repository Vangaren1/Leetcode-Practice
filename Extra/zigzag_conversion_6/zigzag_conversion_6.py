from typing import Optional, List
import copy


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        row = [
            "",
        ] * len(s)
        grid = []
        for i in range(numRows):
            grid.append(copy.deepcopy(row))

        directions = ((1, 0), (-1, 1), (-1, 0), (-1, 1))

        dirIndex = 0
        pos = (0, 0)

        queue = [ch for ch in s]
        grid[0][0] = queue.pop(0)

        while queue:
            curr = queue.pop(0)
            y, x = pos
            dir = directions[dirIndex % 4]
            ny = y + dir[0]
            nx = x + dir[1]
            # check if outside bounds
            while ny < 0 or ny == numRows:
                dirIndex += 1
                dir = directions[dirIndex % 4]
                ny = y + dir[0]
                nx = x + dir[1]
            grid[ny][nx] = curr
            pos = (ny, nx)

        tmp = ""

        for r in grid:
            tmp += "".join(r)

        return tmp


if __name__ == "__main__":
    sol = Solution()

    s = "PAYPALISHIRING"
    numRows = 3

    print(sol.convert(s, numRows))
    print("Running Solution...")
