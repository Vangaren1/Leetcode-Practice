from typing import Optional, List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        height = len(board)
        width = len(board[0])
        diff = ((0, 1), (0, -1), (1, 0), (-1, 0))
        if height < 3 or width < 3:
            return

        seen = set()
        ignore = set()

        def bfs(pos):

            queue = deque()
            queue.append(pos)

            hitEdge = False
            while queue:
                y, x = queue.popleft()
                seen.add((y, x))
                for dy, dx in diff:
                    ny, nx = dy + y, dx + x
                    # otherwise, add the "O"s to the queue to find all connected ones
                    if (
                        0 <= ny < height
                        and 0 <= nx < width
                        and (ny, nx) not in seen
                        and (ny, nx) not in queue
                        and board[ny][nx] == "O"
                    ):
                        queue.append((ny, nx))
                        if (
                            ny == 0
                            or nx == 0
                            or ny == (height - 1)
                            or (nx == width - 1)
                        ):
                            hitEdge = True

            for y, x in seen:
                if not hitEdge and (y, x) not in ignore:
                    board[y][x] = "X"
                else:
                    ignore.add((y, x))

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                if (y, x) not in seen and board[y][x] == "O":
                    bfs((y, x))


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
        ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"],
        ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
        ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],
        ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
        ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
        ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
        ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],
        ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
    ]
    sol.solve(board)
    for b in board:
        print(b)
    print("Running Solution...")
