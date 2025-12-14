from typing import Optional, List


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        sCount = corridor.count("S")
        if sCount % 2 != 0:
            return 0

        pass


if __name__ == "__main__":
    sol = Solution()
    corridor = "SSPPSPS"

    print(sol.numberOfWays(corridor))
    print("Running Solution...")
