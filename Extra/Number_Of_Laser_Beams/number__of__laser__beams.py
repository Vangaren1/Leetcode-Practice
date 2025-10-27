from typing import Optional, List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        last = 0
        for row in bank:
            c = row.count("1")
            if c == 0:
                continue
            total += c * last
            last = c
        return total


if __name__ == "__main__":
    sol = Solution()
    bank = [
        "011001",
        "000000",
        "010100",
        "001000",
    ]
    print(sol.numberOfBeams(bank))
    print("Running Solution...")
