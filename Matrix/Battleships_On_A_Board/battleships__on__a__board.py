from typing import Optional, List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        total = 0
        height = len(board)
        width = len(board[0])

        def bfs(pos):
            queue = [pos]
            diff = ((0, 1), (0, -1), (1, 0), (-1, 0))
            while queue:
                y, x = queue.pop(0)
                board[y][x] = total
                for dy, dx in diff:
                    ny, nx = dy + y, dx + x
                    if 0 <= ny < height and 0 <= nx < width and board[ny][nx] == "X":
                        queue.append((ny, nx))

        for y in range(height):
            for x in range(width):
                if board[y][x] == "X":
                    total += 1
                    bfs((y, x))
        return total


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["X", ".", ".", "X"],
        [".", ".", ".", "X"],
        [".", ".", ".", "X"],
    ]
    print(sol.countBattleships(board))
    print("Running Solution...")
