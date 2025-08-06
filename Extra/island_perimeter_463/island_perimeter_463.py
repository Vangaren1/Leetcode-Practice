from typing import Optional, List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        seen = set()
        height = len(grid)
        width = len(grid[0])

        def bfs(node):
            nonlocal seen, count, height, width
            dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            queue = [node]

            while queue:
                y, x = queue.pop(0)
                if (y, x) in seen:
                    continue
                seen.add((y, x))
                for dy, dx in dir:
                    ny = dy + y
                    nx = dx + x
                    if 0 <= ny < height and 0 <= nx < width:
                        if grid[ny][nx] == 0:
                            count += 1
                        elif (ny, nx) not in seen:
                            queue.append((ny, nx))
                    else:
                        count += 1

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1 and (y, x) not in seen:
                    bfs((y, x))
                    return count

        return count


if __name__ == "__main__":
    sol = Solution()

    grid = [[1, 1, 0], [1, 1, 0]]

    result = sol.islandPerimeter(grid)
    print("Running Solution...")
    print("result: {}".format(result))
