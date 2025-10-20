from typing import Optional, List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        step = 0
        results = []

        for row in range(len(grid)):
            r = range(len(grid[0])) if row % 2 == 0 else range(len(grid[0]) - 1, -1, -1)
            for col in r:
                if step % 2 == 0:
                    results.append(grid[row][col])
                step += 1
        return results


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print(sol.zigzagTraversal(grid))
    print("Running Solution...")
