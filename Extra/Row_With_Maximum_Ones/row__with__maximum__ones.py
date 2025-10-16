from typing import Optional, List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        found = [-1, -1]

        for index in range(len(mat)):
            c = mat[index].count(1)
            if c > found[1]:
                found = [index, c]
        return found
        pass


if __name__ == "__main__":
    sol = Solution()
    mat = [[0, 0, 0], [0, 1, 1]]
    print(sol.rowAndMaximumOnes(mat))
    print("Running Solution...")
