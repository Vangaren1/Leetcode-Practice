from typing import Optional, List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def findPawn(y, x):
            total = 0
            diff = ((0, -1), (0, 1), (1, 0), (-1, 0))

            for dy, dx in diff:
                ny, nx = y + dy, x + dx

                while 0 <= nx < 8 and 0 <= ny < 8 and board[ny][nx] != "B":
                    if board[ny][nx] == "p":
                        total += 1
                        break
                    ny, nx = ny + dy, nx + dx
            return total

        for y in range(8):
            for x in range(8):
                if board[y][x] == "R":
                    return findPawn(y, x)
        return 0


if __name__ == "__main__":
    sol = Solution()
    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", "R", ".", ".", ".", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
    ]
    print(sol.numRookCaptures(board))
    print("Running Solution...")
