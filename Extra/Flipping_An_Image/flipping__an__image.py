from typing import Optional, List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        tmp = [[1 if t == 0 else 0 for t in row] for row in image]
        tmp = [row[::-1] for row in tmp]
        return tmp


if __name__ == "__main__":
    sol = Solution()
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    r = sol.flipAndInvertImage(image)
    for row in r:
        print(r)
    print("Running Solution...")
