from typing import Optional, List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rCount = [sum(row) for row in mat]
        cCount = [sum(row[i] for row in mat) for i in range(len(mat[0]))]
        total = 0
        for y in range(len(mat)):
            for x in range(len(mat[0])):
                if mat[y][x] == 1 and rCount[y] == 1 and cCount[x] == 1:
                    total += 1
        return total


if __name__ == "__main__":
    sol = Solution()
    mat = [
        [1, 0, 0],
        [0, 0, 1],
        [1, 0, 0],
    ]
    print(sol.numSpecial(mat))
    print("Running Solution...")
