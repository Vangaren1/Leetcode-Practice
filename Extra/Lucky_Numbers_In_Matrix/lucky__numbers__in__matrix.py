from typing import Optional, List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minRow = [min(r) for r in matrix]
        minCol = [max([row[k] for row in matrix]) for k in range(len(matrix[0]))]
        results = []
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                curr = matrix[y][x]
                if curr == minRow[y] and curr == minCol[x]:
                    results.append(curr)
        return results


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [3, 7, 8],
        [9, 11, 13],
        [15, 16, 17],
    ]
    print(sol.luckyNumbers(matrix))
    print("Running Solution...")
