from typing import Optional, List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        count = 1
        matrix = [[0] * n for _ in range(n)]

        direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dirPos = 0
        seen = set()
        y, x = 0, 0

        while count <= n * n:
            matrix[y][x] = count

            seen.add((y, x))
            count += 1
            dy, dx = direction[dirPos]

            y, x = dy + y, dx + x

            if (y, x) in seen or y == n or y < 0 or x < 0 or x == n:
                y, x = y - dy, x - dx
                dirPos = (dirPos + 1) % 4
                dy, dx = direction[dirPos]
                y, x = y + dy, x + dx

        return matrix

        pass


if __name__ == "__main__":
    sol = Solution()
    r = sol.generateMatrix(3)
    for row in r:
        print(row)
    print("Running Solution...")
