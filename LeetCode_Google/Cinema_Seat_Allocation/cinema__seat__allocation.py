from typing import Optional, List
import heapq, bisect
from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rowDict = defaultdict(set)

        for row, seat in reservedSeats:
            rowDict[row].add(seat)

        count = (n - len(rowDict)) * 2

        for row, seatSet in rowDict.items():
            blocks = {1, 2, 3}
            for seat in seatSet:
                if seat in (1, 10):
                    continue
                if seat in (2, 3):
                    blocks.discard(1)
                elif seat in (4, 5):
                    blocks.discard(1)
                    blocks.discard(2)
                elif seat in (6, 7):
                    blocks.discard(2)
                    blocks.discard(3)
                elif seat in (8, 9):
                    blocks.discard(3)

            if len(blocks) == 3:
                count += 2
            elif 1 in blocks and 3 in blocks:
                count += 2
            elif blocks:
                count += 1

        return count

        pass


if __name__ == "__main__":
    sol = Solution()
    n = 2
    reservedSeats = [[2, 1], [1, 8], [2, 6]]
    print(sol.maxNumberOfFamilies(n, reservedSeats))
    print("Running Solution...")
