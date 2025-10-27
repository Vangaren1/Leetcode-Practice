from typing import Optional, List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        original = [board[i].copy() for i in range(len(board))]
        # for row in original:
        #     print(row)
        height = len(board)
        width = len(board[0])

        def countNeighbors(y, x):
            count = 0
            top, bottom, left, right = False, False, False, False

            if y > 0:
                count += original[y - 1][x]
                top = True
            if y < height - 1:
                count += original[y + 1][x]
                bottom = True
            if x > 0:
                count += original[y][x - 1]
                left = True
            if x < width - 1:
                count += original[y][x + 1]
                right = True
            if top:
                if left:
                    count += original[y - 1][x - 1]
                if right:
                    count += original[y - 1][x + 1]
            if bottom:
                if left:
                    count += original[y + 1][x - 1]
                if right:
                    count += original[y + 1][x + 1]
            return count

        for y in range(height):
            for x in range(width):

                neighbors = countNeighbors(y, x)
                if original[y][x] == 1:
                    if neighbors < 2:
                        board[y][x] = 0
                    elif neighbors > 3:
                        board[y][x] = 0
                elif neighbors == 3:
                    board[y][x] = 1


if __name__ == "__main__":
    sol = Solution()
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0],
    ]
    sol.gameOfLife(board)
    print()
    for row in board:
        print(row)
    print("Running Solution...")
