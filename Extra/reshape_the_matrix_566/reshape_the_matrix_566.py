from typing import Optional, List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        height = len(mat)
        width = len(mat[0])

        def getPos(n):
            y = n // width
            x = n % width
            ny = n // c
            nx = n % c
            return (y, x, ny, nx)

        if (height * width) != (r * c) or (height == r and c == width):
            return mat

        cCol = [0] * c

        newMat = [cCol.copy() for _ in range(r)]

        for n in range(height * width):
            y, x, ny, nx = getPos(n)
            print(f"{y}, {x}, {ny}, {nx}")
            newMat[ny][nx] = mat[y][x]

        return newMat


if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    for row in sol.matrixReshape(mat, r, c):
        print(row)
    print("Running Solution...")
