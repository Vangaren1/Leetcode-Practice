from typing import Optional, List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[None] * 3 for _ in range(3)]

        step = 0

        for y, x in moves:
            board[y][x] = "A" if step % 2 == 0 else "B"
            step += 1

        # check rows
        for r in board:
            if len(set(r)) == 1 and all(r):
                return r[0]
        # check columns
        for c in range(3):
            col = [board[y][c] for y in range(3)]
            if len(set(col)) == 1 and all(col):
                return col[0]
        # check diagonal
        leftToRight = [board[0][0], board[1][1], board[2][2]]
        rightToLeft = [board[0][2], board[1][1], board[2][0]]
        if len(set(leftToRight)) == 1 and all(leftToRight):
            return leftToRight[0]
        if len(set(rightToLeft)) == 1 and all(rightToLeft):
            return rightToLeft[0]

        return "Draw" if step == 9 else "Pending"


if __name__ == "__main__":
    sol = Solution()
    moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    print(sol.tictactoe(moves))

    print("Running Solution...")
