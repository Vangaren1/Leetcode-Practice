from typing import Optional, List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up = True
        retVal = []
        height = len(mat)
        width = len(mat[0])
        total = height * width

        y, x = 0, 0

        while total > 0:
            while 0 <= y < height and 0 <= x < width:
                retVal.append(mat[y][x])
                total -= 1
                if up:
                    y -= 1
                    x += 1
                else:
                    y += 1
                    x -= 1
            if up:
                if x == width:
                    x -= 1
                    y += 2
                if y < 0 and x != width:
                    y += 1
            else:
                if y == height:
                    y -= 1
                    x += 2
                if x < 0 and y != height:
                    x += 1

            up = not up

        return retVal


if __name__ == "__main__":
    sol = Solution()
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    # [1,2,4,7,5,3,6,8,9]
    r = sol.findDiagonalOrder(mat)
    print(r)
    print("Running Solution...")
