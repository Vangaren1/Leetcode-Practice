from typing import Optional, List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        check0 = []
        check90 = []
        check180 = []
        check270 = []

        for y in range(n):
            r = []  # -90
            for x in range(n):
                check0.append(mat[y][x] == target[y][x])
                check90.append(mat[n - x - 1][y] == target[y][x])
                check180.append(mat[n - y - 1][n - x - 1] == target[y][x])
                check270.append(mat[x][n - y - 1] == target[y][x])

        return all(check90) or all(check180) or all(check270) or all(check0)

        pass


if __name__ == "__main__":
    sol = Solution()
    mat = [[0, 1], [1, 0]]
    target = [[1, 0], [0, 1]]
    print(sol.findRotation(mat, target))
    print("Running Solution...")
