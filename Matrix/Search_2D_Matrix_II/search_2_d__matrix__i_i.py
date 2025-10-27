from typing import Optional, List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        height = len(matrix)
        width = len(matrix[0])

        for y in range(height):
            if matrix[y][0] > target:
                break
            for x in range(width):
                if matrix[y][x] == target:
                    return True
                if matrix[y][x] > target:
                    break
        return False

        pass


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    target = 5

    print(sol.searchMatrix(matrix, target))

    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    target = 20

    print(sol.searchMatrix(matrix, target))
    print("Running Solution...")
