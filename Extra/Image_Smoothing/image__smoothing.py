from typing import Optional, List
import math


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        height = len(img)
        width = len(img[0])

        newImg = [[0] * width for _ in range(height)]

        def smooth(y, x):
            count = 0
            total = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= y + i < height and 0 <= x + j < width:
                        count += 1
                        total += img[y + i][j + x]
            return math.floor(total / count)

        for y in range(height):
            for x in range(width):
                newImg[y][x] = smooth(y, x)

        return newImg


if __name__ == "__main__":
    sol = Solution()
    img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
    s = sol.imageSmoother(img)
    for r in s:
        print(r)
    print("Running Solution...")
