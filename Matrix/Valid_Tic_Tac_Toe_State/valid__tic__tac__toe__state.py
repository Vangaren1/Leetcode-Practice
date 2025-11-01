from typing import Optional, List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        countO = 0
        countX = 0

        for row in board:
            countO += row.count("O")
            countX += row.count("X")

        # X must play first
        if countX == 0 and countO >= 1:
            return False

        # must take turns
        if (countX - countO) not in (0, 1):
            return False

        # if countX + countO == 9:
        #     return True

        # check for 3 in a row, column, or diagonal
        threeInARowCountX = 0
        threeInARowCountO = 0
        first, second, third = [], [], []
        for row in board:
            if row.count("O") == 3:
                threeInARowCountO += 1
            if row.count("X") == 3:
                threeInARowCountX += 1
            first.append(row[0])
            second.append(row[1])
            third.append(row[2])
        leftToRight = [board[0][0], board[1][1], board[2][2]]
        rightToLeft = [board[0][2], board[1][1], board[2][0]]

        if first.count("O") == 3:
            threeInARowCountO += 1
        if first.count("X") == 3:
            threeInARowCountX += 1
        if second.count("O") == 3:
            threeInARowCountO += 1
        if second.count("X") == 3:
            threeInARowCountX += 1

        if third.count("O") == 3:
            threeInARowCountO += 1
        if third.count("X") == 3:
            threeInARowCountX += 1
        if leftToRight.count("O") == 3:
            threeInARowCountO += 1
        if leftToRight.count("X") == 3:
            threeInARowCountX += 1
        if rightToLeft.count("O") == 3:
            threeInARowCountO += 1
        if rightToLeft.count("X") == 3:
            threeInARowCountX += 1

        if threeInARowCountX in (1, 2) and threeInARowCountO in (1, 2):
            return False

        if threeInARowCountX in (1, 2) and (countX - countO) != 1:
            return False

        if threeInARowCountO == 1 and (countX - countO) == 1:
            return False

        return True
        pass


if __name__ == "__main__":
    sol = Solution()
    board = ["OO ", "O X", "X  "]
    print(sol.validTicTacToe(board))
    print("Running Solution...")
