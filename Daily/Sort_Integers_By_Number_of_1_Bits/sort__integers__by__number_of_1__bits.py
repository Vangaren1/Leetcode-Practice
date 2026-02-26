from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bitCount = [{bin(n).count("1"), n} for n in arr]
        bitCount.sort()
        return [n[1] for n in bitCount]
        pass


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
