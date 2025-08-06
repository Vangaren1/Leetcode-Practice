from typing import Optional, List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSets = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        squareSets = [
            [set(), set(), set()],
            [set(), set(), set()],
            [set(), set(), set()],
        ]
        for y in range(9):
            testSet = set()
            for x in range(9):
                curr = board[y][x]
                squareX = x // 3
                squareY = y // 3
                # print(
                #     "x, y: ({},{})  squarex, squareY ({},{})".format(
                #         x, y, squareY, squareX
                #     )
                # )
                if curr.isdigit():
                    if (
                        curr not in testSet
                        and curr not in colSets[x]
                        and curr not in squareSets[squareY][squareX]
                    ):
                        testSet.add(curr)
                        colSets[x].add(curr)
                        squareSets[squareY][squareX].add(curr)
                    else:
                        return False

        return True

        pass


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    sol.isValidSudoku(board)
    print("Running Solution...")
