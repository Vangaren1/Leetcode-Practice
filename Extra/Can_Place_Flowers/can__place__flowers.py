from typing import Optional, List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)

        if n == 0 and l >= 1:
            return True

        if l < 2 and n <= 1:
            return 1 not in flowerbed
        if n > l // 2:
            return False

        ptr = 0

        while ptr < l:
            if flowerbed[ptr] == 1:
                ptr += 2
            elif ptr < l - 1 and flowerbed[ptr + 1] == 1:
                ptr += 3
            else:
                n -= 1
                ptr += 2

        return n <= 0


if __name__ == "__main__":
    sol = Solution()

    # flowerbed = [1, 0, 0, 0, 1]

    # print(sol.canPlaceFlowers(flowerbed, 2))
    # print(sol.canPlaceFlowers(flowerbed, 1))

    # flowerbed = [1, 0, 0, 0, 1, 0, 0]

    # print(sol.canPlaceFlowers(flowerbed, 2))

    print(sol.canPlaceFlowers([0, 0, 0], 2))
    print("Running Solution...")
