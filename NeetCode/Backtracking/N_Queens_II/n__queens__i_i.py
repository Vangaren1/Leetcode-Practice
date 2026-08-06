from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def totalNQueens(self, n: int) -> int:

        col = set()
        posDiag = set()
        negDiag = set()

        count = 0

        def backtrack(row):
            nonlocal count

            if row == n:
                count += 1
                return

            for c in range(n):
                if c in col or row - c in posDiag or row + c in negDiag:
                    continue

                col.add(c)
                posDiag.add(row - c)
                negDiag.add(row + c)

                backtrack(row + 1)

                col.remove(c)
                posDiag.remove(row - c)
                negDiag.remove(row + c)

        backtrack(0)

        return count

        pass


if __name__ == "__main__":
    sol = Solution()
    for i in range(10):
        print(sol.totalNQueens(i))
    print("Running Solution...")


"""  
class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."] * n for _ in range(n)]

        columns = set()
        posDiag = set()
        negDiag = set()

        results = []

        def backtrack(row):
            if row == n:
                c = ["".join(r) for r in board]
                results.append(c)
                return
            for col in range(n):
                pDiag = row + col
                nDiag = row - col
                if col in columns or pDiag in posDiag or nDiag in negDiag:
                    continue

                columns.add(col)
                posDiag.add(pDiag)
                negDiag.add(nDiag)
                board[row][col] = "Q"

                backtrack(row + 1)

                columns.remove(col)
                posDiag.remove(pDiag)
                negDiag.remove(nDiag)
                board[row][col] = "."

        backtrack(0)
        return len(results)
"""
