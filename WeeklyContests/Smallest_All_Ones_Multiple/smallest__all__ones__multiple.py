from typing import Optional, List


class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        curr = 0

        for l in range(1, k + 1):

            curr = (curr * 10 + 1) % k
            if curr == 0:
                return l

        return -1


if __name__ == "__main__":
    sol = Solution()

    print(sol.minAllOneMultiple(5))

    # assert sol.minAllOneMultiple(3) == 3
    # assert sol.minAllOneMultiple(7) == 6
    # assert sol.minAllOneMultiple(2) == -1
    print("Running Solution...")
