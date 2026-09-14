from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ptr = 0
        count = 0
        while ptr < len(flowerbed):
            print(f"{ptr}")
            if count >= n:
                return True
            # check for front end
            if flowerbed[ptr] == 0:

                if (
                    (ptr == 0 and flowerbed[1] == 0)
                    or (ptr == len(flowerbed) - 1 and flowerbed[ptr - 1] == 0)
                    or (
                        0 < ptr < len(flowerbed) - 1
                        and flowerbed[ptr - 1] == 0
                        and flowerbed[ptr + 1] == 0
                    )
                ):
                    count += 1
                    ptr += 2
                    continue
                else:
                    ptr += 1
            else:
                ptr += 1

        return count >= n


if __name__ == "__main__":
    sol = Solution()
    flowerbed = [1, 0, 1, 0, 0]
    print(sol.canPlaceFlowers(flowerbed, 1))
    print("Running Solution...")
