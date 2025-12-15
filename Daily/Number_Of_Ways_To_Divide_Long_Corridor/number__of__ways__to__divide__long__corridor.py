from typing import Optional, List


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        if n < 2:
            return 0

        sCount = corridor.count("S")
        if sCount % 2 != 0 or sCount < 2:
            return 0

        MOD = 10**9 + 7
        seen = 0
        total = 1
        plantCount = 0
        countingPlants = False
        ptr1, ptr2 = 0, 0

        for ch in corridor:
            if ch == "S":
                seen += 1

                if seen > 2 and seen % 2 == 1:
                    total = (total * (plantCount + 1)) % MOD

                plantCount = 0
                countingPlants = seen % 2 == 0
            else:
                if countingPlants:
                    plantCount += 1
        return total

        pass


if __name__ == "__main__":
    sol = Solution()
    corridor = "SSPPSPS"

    print(sol.numberOfWays(corridor))
    print("Running Solution...")
