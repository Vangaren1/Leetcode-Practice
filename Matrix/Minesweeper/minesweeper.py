from typing import Optional, List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        y, x = click
        height = len(board)
        width = len(board[0])

        if board[y][x] == "M":
            board[y][x] = "X"
            return board

        diff = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1))

        def count(pos):
            y, x = pos
            total = 0
            for dy, dx in diff:
                ny, nx = y + dy, x + dx
                if 0 <= ny < height and 0 <= nx < width and board[ny][nx] == "M":
                    total += 1
            return total

        def bfs(pos):

            queue = [pos]
            seen = set()

            while queue:
                y, x = queue.pop(0)
                seen.add((y, x))
                if board[y][x] == "E":
                    c = count((y, x))
                    board[y][x] = "B" if c == 0 else str(c)
                    for dy, dx in diff:
                        ny, nx = y + dy, x + dx
                        if (
                            0 <= ny < height
                            and 0 <= nx < width
                            and (ny, nx) not in queue
                            and (ny, nx) not in seen
                            and c == 0
                        ):
                            queue.append((ny, nx))

        bfs((y, x))

        return board

        pass


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["E", "E", "E", "E", "E"],
        ["E", "E", "M", "E", "E"],
        ["E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E"],
    ]
    click = [3, 0]
    print(sol.updateBoard(board, click))
    print("Running Solution...")
