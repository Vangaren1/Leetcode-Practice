from typing import Optional, List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        one = [grid[0][0], grid[0][1], grid[1][0], grid[1][1]]
        two = [grid[0][1], grid[1][1], grid[0][2], grid[1][2]]
        three = [grid[1][0], grid[1][1], grid[2][0], grid[2][1]]
        four = [grid[1][1], grid[1][2], grid[2][1], grid[2][2]]
        for block in [one, two, three, four]:
            if block.count("B") == 3 or block.count("W") == 3:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    grid = [["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]
    print(sol.canMakeSquare(grid))
    print("Running Solution...")
