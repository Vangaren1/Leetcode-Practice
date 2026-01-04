from typing import Optional, List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        typesOfCandy = set(candyType)
        numberOfCandy = len(candyType)

        mCandy = numberOfCandy // 2

        return min(typesOfCandy, mCandy)


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
