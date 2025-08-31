from typing import Optional, List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [
            [
                ".",
            ]
            * n
        ] * n

        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(4))
    print("Running Solution...")
