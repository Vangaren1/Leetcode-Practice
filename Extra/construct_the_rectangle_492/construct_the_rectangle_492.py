from typing import Optional, List
import math


class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        # see if it's a perfect square
        sq = math.isqrt(area)

        left = sq
        while area % left != 0 and left > 0:
            left -= 1

        right = area // left

        return [left, right]


if __name__ == "__main__":
    sol = Solution()
    print(sol.constructRectangle(122122))
    print("Running Solution...")
