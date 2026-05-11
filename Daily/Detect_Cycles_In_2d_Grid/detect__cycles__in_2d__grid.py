from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        height = len(grid)
        width = len(grid[0])
        dir = ((0, 1), (0, -1), (1, 0), (-1, 0))
        opp = {
            (0, 1): (0, -1),
            (1, 0): (-1, 0),
            (0, -1): (0, 1),
            (-1, 0): (1, 0),
        }
        count = 0

        def dfs(pos, prev):
            # prev = dir index of previous node
            y, x = pos
            curr = grid[y][x]
            if curr == count:
                return True
            grid[y][x] = count
            for index, d in enumerate(dir):
                if index == opp.get(prev):
                    continue
                dy, dx = d
                ny, nx = dy + y, dx + x
                if 0 <= ny < height and 0 <= nx < width:
                    if grid[ny][nx] == count:
                        return True
                    if grid[ny][nx] == curr:
                        if dfs((ny, nx), index):
                            return True

            return False

        for y in range(height):
            for x in range(width):
                if type(grid[y][x]) == type("a"):
                    if dfs((y, x), None):
                        return True
                    count += 1
        return False

        pass


if __name__ == "__main__":
    sol = Solution()
    grid = [
        ["a", "b", "b"],
        ["b", "z", "b"],
        ["b", "b", "a"],
    ]
    print(sol.containsCycle(grid))
    print("Running Solution...")
