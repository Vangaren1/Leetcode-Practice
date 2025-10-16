from typing import Optional, List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        total = 0

        while grid[0]:
            tmp = []

            for row in range(len(grid)):
                val = max(grid[row])
                idx = grid[row].index(val)
                grid[row].pop(idx)
                tmp.append(val)
            total += max(tmp)
        return total

        pass


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [1, 2, 4],
        [3, 3, 1],
    ]
    print(sol.deleteGreatestValue(grid))
    print("Running Solution...")
