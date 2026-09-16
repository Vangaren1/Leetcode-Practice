from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        height = len(img1)
        width = len(img1[0])

        def convertToBitmask(img):
            bimg = []
            for row in img:
                mask = 0
                for bit in row:
                    mask = (mask << 1) | bit
                bimg.append(mask)
            return bimg

        bimg1 = convertToBitmask(img1)[::-1]
        bimg2 = convertToBitmask(img2)[::-1]

        def calcOverlap(second):
            # print(f"overlap between {bimg1} and {second}")
            count = 0
            for index, val in enumerate(bimg1):
                overlap = val & second[index]
                count += overlap.bit_count()
            return count

        best = 0

        for y in range(height):
            for x in range(width):
                # translate the second img y items up, and x to the right , then compare
                testRight = bimg2[:]
                testLeft = bimg2[:]
                testRight = [row >> x for row in testRight]
                testLeft = [row << x for row in testLeft]
                for test in [testRight, testLeft]:
                    up = test[y:] + [0] * y
                    down = [0] * y + test[: height - y]
                    best = max(best, calcOverlap(up))
                    best = max(best, calcOverlap(down))

        return best

        pass


if __name__ == "__main__":
    sol = Solution()
    img1 = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]
    img2 = [
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 1],
    ]
    print(sol.largestOverlap(img1, img2))
    print("Running Solution...")
