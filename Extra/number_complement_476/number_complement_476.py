from typing import Optional, List


class Solution:
    def findComplement(self, num: int) -> int:
        length = len(bin(num)) - 2
        bitmask = (1 << length) - 1
        return bitmask ^ num


if __name__ == "__main__":
    sol = Solution()
    print(sol.findComplement(5))
    print(sol.findComplement(1))
    print("Running Solution...")
