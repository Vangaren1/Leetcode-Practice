from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ia = int(a, 2)
        ib = int(b, 2)
        return bin(ia + ib)[2:]
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary("101", "11"))
    print("Running Solution...")
