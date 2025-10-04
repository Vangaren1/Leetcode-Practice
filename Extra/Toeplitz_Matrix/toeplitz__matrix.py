from typing import Optional, List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        height = len(matrix)
        width = len(matrix[0])

        seen = set()

        for y in range(height):
            for x in range(width):
                if (y, x) not in seen:
                    tmp = matrix[y][x]
                    i, j = y, x
                    while 0 <= i < height and 0 <= j < width:
                        if matrix[i][j] != tmp:
                            return False
                        seen.add((i, j))
                        i += 1
                        j += 1

        return True


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 4, 1, 2]]
    print(sol.isToeplitzMatrix(matrix))
    print("Running Solution...")
